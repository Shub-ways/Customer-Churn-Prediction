import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(base_dir / "streamlit"))

from utils.preprocessing import format_prediction_input, FEATURE_COLUMNS

def test_format_prediction_input():
    df = format_prediction_input(
        complains=0,
        subscription_length=38,
        frequency_of_use=71,
        seconds_of_use=4370,
        distinct_called_numbers=17,
        status=1,
        customer_value=197.64,
        frequency_of_sms=5
    )
    
    assert len(df) == 1
    assert list(df.columns) == FEATURE_COLUMNS
    assert df.loc[0, 'Complains'] == 0
    assert df.loc[0, 'Subscription Length'] == 38
    assert df.loc[0, 'Customer_Engagement'] == 76  # 71 + 5
    assert round(df.loc[0, 'Average_Call_Duration'], 2) == 61.55
