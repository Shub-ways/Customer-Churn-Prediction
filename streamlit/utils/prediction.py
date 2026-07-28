import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import streamlit as st

@st.cache_resource
def load_model():
    """
    Loads pre-trained XGBoost Churn Prediction model from models/customer_churn_model.pkl
    """
    base_dir = Path(__file__).resolve().parents[2]
    model_path = base_dir / "models" / "customer_churn_model.pkl"
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return joblib.load(model_path)

def predict_churn(input_df: pd.DataFrame):
    """
    Predicts churn class and churn probability for input features DataFrame.
    Returns (prediction_class, probability_churn, risk_tier).
    """
    model = load_model()
    prob = float(model.predict_proba(input_df)[0][1])
    pred = int(model.predict(input_df)[0])

    if prob < 0.35:
        risk_tier = "Low Risk"
    elif prob < 0.65:
        risk_tier = "Medium Risk"
    else:
        risk_tier = "High Risk"

    return pred, prob, risk_tier

def batch_predict_churn(df: pd.DataFrame) -> pd.DataFrame:
    """
    Runs model predictions on a DataFrame of customers and returns copy with
    'Predicted_Churn', 'Churn_Probability', and 'Risk_Tier' appended.
    """
    model = load_model()
    feature_cols = [
        'Complains', 'Subscription Length', 'Frequency of use', 'Seconds of Use',
        'Distinct Called Numbers', 'Customer_Engagement', 'Average_Call_Duration',
        'Status', 'Revenue_Per_Month', 'Customer Value'
    ]
    
    # Ensure missing columns are computed if needed
    result_df = df.copy()
    if 'Customer_Engagement' not in result_df.columns and 'Frequency of use' in result_df.columns:
        sms = result_df['Frequency of SMS'] if 'Frequency of SMS' in result_df.columns else 0
        result_df['Customer_Engagement'] = result_df['Frequency of use'] + sms
    if 'Average_Call_Duration' not in result_df.columns and 'Seconds of Use' in result_df.columns:
        freq = result_df['Frequency of use'].replace(0, 1)
        result_df['Average_Call_Duration'] = result_df['Seconds of Use'] / freq
    if 'Revenue_Per_Month' not in result_df.columns and 'Customer Value' in result_df.columns:
        sub = result_df['Subscription Length'].replace(0, 1)
        result_df['Revenue_Per_Month'] = result_df['Customer Value'] / sub

    model_input = result_df[feature_cols]
    probs = model.predict_proba(model_input)[:, 1]
    preds = model.predict(model_input)
    
    tiers = []
    for p in probs:
        if p < 0.35:
            tiers.append("Low Risk")
        elif p < 0.65:
            tiers.append("Medium Risk")
        else:
            tiers.append("High Risk")
            
    result_df['Predicted_Churn'] = preds
    result_df['Churn_Probability'] = np.round(probs * 100, 2)
    result_df['Risk_Tier'] = tiers
    return result_df

def get_feature_contributions(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes approximate feature risk contributions based on model importances & sample values.
    """
    model = load_model()
    importances = model.feature_importances_
    features = input_df.columns
    
    # Estimate relative risk contribution
    values = input_df.iloc[0].values
    
    contrib_data = []
    for feat, imp, val in zip(features, importances, values):
        contrib_data.append({
            'Feature': feat,
            'Value': val,
            'Importance_Weight': float(imp)
        })
        
    df_contrib = pd.DataFrame(contrib_data).sort_values(by='Importance_Weight', ascending=True)
    return df_contrib
