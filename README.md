Customer Churn Prediction & Business Insights Dashboard
Project Overview

Developed an end-to-end Machine Learning solution to predict customer churn and identify the major factors influencing customer retention. The project includes data preprocessing, feature engineering, predictive modeling, explainability analysis, SQL-based business insights, and an interactive Power BI dashboard.

Problem Statement

Customer churn directly impacts business revenue and profitability. The objective of this project is to identify customers who are likely to churn and recommend proactive retention strategies using machine learning.

Dataset
Source: UCI Machine Learning Repository
Domain: Telecommunications
Records: 2,850
Features: 13 (after preprocessing)
Tech Stack
Programming
Python
SQL
Libraries
Pandas
NumPy
Scikit-learn
XGBoost
Matplotlib
SHAP / Permutation Importance
Visualization
Power BI
Machine Learning Pipeline
Data Cleaning
Feature Engineering
Exploratory Data Analysis
Feature Selection
Model Training
Hyperparameter Evaluation
Model Explainability
Business Insights
Dashboard Development
Models Evaluated
Model	Accuracy
Random Forest	94.04%
XGBoost	94.04%
Gradient Boosting	93.16%
Decision Tree	92.10%
Logistic Regression	90.94%
Best Model

Random Forest Classifier

Accuracy: 94.04%
Precision: 86.67%
Recall: 75.28%
F1 Score: 79.29%
ROC-AUC: 97.31%
Dashboard Features
Executive Dashboard
Customer KPIs
Churn Distribution
Customer Segmentation
Interactive Filters
Customer Insights
Complaint Analysis
Usage Behavior
Customer Value
Engagement Analysis
Model Insights
Model Comparison
Feature Importance
Confusion Matrix
ROC Curve
Performance Metrics
Business Recommendations
Key Findings
Business Goals
Actionable Recommendations
Expected Business Impact
Key Business Insights
Complaint history is the strongest indicator of churn.
Inactive customers are at significantly higher churn risk.
Customer engagement strongly influences retention.
Early intervention can substantially improve retention rates.
Future Enhancements
Real-time churn prediction API using Flask/FastAPI
Automated email alerts for high-risk customers
Cloud deployment on Azure or AWS
Continuous model monitoring and retraining