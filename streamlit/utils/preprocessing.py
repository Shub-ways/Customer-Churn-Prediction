import pandas as pd

FEATURE_COLUMNS = [
    'Complains',
    'Subscription Length',
    'Frequency of use',
    'Seconds of Use',
    'Distinct Called Numbers',
    'Customer_Engagement',
    'Average_Call_Duration',
    'Status',
    'Revenue_Per_Month',
    'Customer Value'
]

def format_prediction_input(
    complains: int,
    subscription_length: int,
    frequency_of_use: int,
    seconds_of_use: int,
    distinct_called_numbers: int,
    status: int,
    customer_value: float,
    frequency_of_sms: int = 0
) -> pd.DataFrame:
    """
    Constructs a DataFrame with all 10 required features for model prediction,
    calculating derived metrics (Customer_Engagement, Average_Call_Duration, Revenue_Per_Month).
    """
    customer_engagement = frequency_of_use + frequency_of_sms
    avg_call_duration = (seconds_of_use / frequency_of_use) if frequency_of_use > 0 else 0.0
    revenue_per_month = (customer_value / subscription_length) if subscription_length > 0 else customer_value

    input_data = {
        'Complains': [int(complains)],
        'Subscription Length': [int(subscription_length)],
        'Frequency of use': [int(frequency_of_use)],
        'Seconds of Use': [int(seconds_of_use)],
        'Distinct Called Numbers': [int(distinct_called_numbers)],
        'Customer_Engagement': [int(customer_engagement)],
        'Average_Call_Duration': [float(avg_call_duration)],
        'Status': [int(status)],
        'Revenue_Per_Month': [float(revenue_per_month)],
        'Customer Value': [float(customer_value)]
    }

    df = pd.DataFrame(input_data)
    return df[FEATURE_COLUMNS]
