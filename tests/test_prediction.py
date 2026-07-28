import sys
import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(base_dir / "streamlit"))

from utils.preprocessing import format_prediction_input
from utils.prediction import predict_churn, batch_predict_churn, get_feature_contributions

def test_predict_churn():
    df = format_prediction_input(
        complains=0,
        subscription_length=38,
        frequency_of_use=71,
        seconds_of_use=4370,
        distinct_called_numbers=17,
        status=1,
        customer_value=197.64
    )
    
    pred, prob, risk_tier = predict_churn(df)
    
    assert pred in [0, 1]
    assert 0.0 <= prob <= 1.0
    assert risk_tier in ["Low Risk", "Medium Risk", "High Risk"]

def test_batch_predict_churn():
    input_data = [
        {'Complains': 0, 'Subscription Length': 38, 'Frequency of use': 71, 'Seconds of Use': 4370, 'Distinct Called Numbers': 17, 'Status': 1, 'Customer Value': 197.64},
        {'Complains': 1, 'Subscription Length': 5, 'Frequency of use': 2, 'Seconds of Use': 50, 'Distinct Called Numbers': 1, 'Status': 2, 'Customer Value': 10.0}
    ]
    df_batch = batch_predict_churn(pd.DataFrame(input_data))
    
    assert len(df_batch) == 2
    assert 'Predicted_Churn' in df_batch.columns
    assert 'Churn_Probability' in df_batch.columns
    assert 'Risk_Tier' in df_batch.columns

def test_get_feature_contributions():
    df = format_prediction_input(
        complains=1,
        subscription_length=12,
        frequency_of_use=10,
        seconds_of_use=200,
        distinct_called_numbers=2,
        status=2,
        customer_value=50.0
    )
    contrib = get_feature_contributions(df)
    
    assert len(contrib) == 10
    assert 'Feature' in contrib.columns
    assert 'Importance_Weight' in contrib.columns
