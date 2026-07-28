import sys
from pathlib import Path
from typing import List

# Ensure parent directory is in sys.path for streamlit/utils imports
base_dir = Path(__file__).resolve().parents[1]
if str(base_dir) not in sys.path:
    sys.path.append(str(base_dir))
if str(base_dir / "streamlit") not in sys.path:
    sys.path.append(str(base_dir / "streamlit"))

from fastapi import FastAPI, HTTPException
from api.schemas import CustomerPredictionInput, PredictionResponse, BatchPredictionResponse
from utils.preprocessing import format_prediction_input
from utils.prediction import predict_churn, batch_predict_churn
import pandas as pd

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production REST API microservice for real-time customer churn probability scoring & risk classification.",
    version="1.0.0"
)

@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "service": "Customer Churn Prediction API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
def predict_single_customer(customer: CustomerPredictionInput):
    try:
        input_df = format_prediction_input(
            complains=customer.Complains,
            subscription_length=customer.Subscription_Length,
            frequency_of_use=customer.Frequency_of_use,
            seconds_of_use=customer.Seconds_of_Use,
            distinct_called_numbers=customer.Distinct_Called_Numbers,
            status=customer.Status,
            customer_value=customer.Customer_Value,
            frequency_of_sms=customer.Frequency_of_SMS
        )
        
        pred_class, probability, risk_tier = predict_churn(input_df)
        
        return PredictionResponse(
            predicted_churn=pred_class,
            churn_probability=round(probability * 100, 2),
            risk_tier=risk_tier
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict_batch", response_model=BatchPredictionResponse, tags=["Prediction"])
def predict_batch_customers(customers: List[CustomerPredictionInput]):
    try:
        records = []
        for c in customers:
            records.append({
                'Complains': c.Complains,
                'Subscription Length': c.Subscription_Length,
                'Frequency of use': c.Frequency_of_use,
                'Seconds of Use': c.Seconds_of_Use,
                'Distinct Called Numbers': c.Distinct_Called_Numbers,
                'Status': c.Status,
                'Customer Value': c.Customer_Value,
                'Frequency of SMS': c.Frequency_of_SMS
            })
        
        raw_df = pd.DataFrame(records)
        res_df = batch_predict_churn(raw_df)
        
        resp_list = []
        for _, row in res_df.iterrows():
            resp_list.append(PredictionResponse(
                predicted_churn=int(row['Predicted_Churn']),
                churn_probability=float(row['Churn_Probability']),
                risk_tier=str(row['Risk_Tier'])
            ))
            
        return BatchPredictionResponse(
            total_records=len(res_df),
            high_risk_count=int((res_df['Risk_Tier'] == 'High Risk').sum()),
            medium_risk_count=int((res_df['Risk_Tier'] == 'Medium Risk').sum()),
            low_risk_count=int((res_df['Risk_Tier'] == 'Low Risk').sum()),
            predictions=resp_list
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
