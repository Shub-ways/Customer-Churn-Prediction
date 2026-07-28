from pydantic import BaseModel, Field
from typing import List

class CustomerPredictionInput(BaseModel):
    Complains: int = Field(..., example=0, description="0 = No Complaint, 1 = Complaint Logged")
    Subscription_Length: int = Field(..., alias="Subscription Length", example=38, description="Subscription tenure in months")
    Frequency_of_use: int = Field(..., alias="Frequency of use", example=71, description="Total number of calls")
    Seconds_of_Use: int = Field(..., alias="Seconds of Use", example=4370, description="Total call duration in seconds")
    Distinct_Called_Numbers: int = Field(..., alias="Distinct Called Numbers", example=17, description="Number of distinct phone numbers called")
    Status: int = Field(..., example=1, description="1 = Active, 2 = Inactive")
    Customer_Value: float = Field(..., alias="Customer Value", example=197.64, description="Customer value metric score")
    Frequency_of_SMS: int = Field(default=0, alias="Frequency of SMS", example=5, description="Total SMS sent")

    class Config:
        populate_by_name = True

class PredictionResponse(BaseModel):
    predicted_churn: int
    churn_probability: float
    risk_tier: str

class BatchPredictionResponse(BaseModel):
    total_records: int
    high_risk_count: int
    medium_risk_count: int
    low_risk_count: int
    predictions: List[PredictionResponse]
