import streamlit as st
from utils.style import apply_custom_css

st.set_page_config(
    page_title="System Architecture & Documentation",
    layout="wide"
)

apply_custom_css()

st.markdown("""
<div class="hero-banner">
    <h1>System Architecture & Documentation</h1>
    <p>Technical specifications, machine learning pipeline workflow, REST API endpoints, and system architecture.</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="equal-card" style="min-height: 255px;">
        <div>
            <h4>Dataset Specifications</h4>
            <p>
                <b>Source</b>: UCI Machine Learning Repository (Telecom Churn Dataset)<br>
                <b>Dataset Size</b>: 2,850 customer records<br>
                <b>Features</b>: 13 raw variables + 3 engineered behavioral metrics<br>
                <b>Target Variable</b>: <code>Churn</code> (0 = Retained, 1 = Churned)<br>
                <b>Domain</b>: Telecommunications Customer Lifecycle & Revenue Assurance
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
    <div class="equal-card" style="min-height: 255px;">
        <div>
            <h4>Engineering & MLOps Tech Stack</h4>
            <p>
                <b>Language</b>: Python 3.10+<br>
                <b>Machine Learning</b>: Scikit-Learn, XGBoost, Joblib<br>
                <b>API Microservice</b>: FastAPI, Pydantic, Uvicorn<br>
                <b>Database & SQL</b>: SQLite 3 Analytics Database<br>
                <b>Web UI Framework</b>: Streamlit, Plotly Express<br>
                <b>Testing & CI/CD</b>: Pytest, GitHub Actions CI
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("### System Architecture & Pipeline Workflow")

st.markdown("""
<div class="custom-card">
    <h4>1. Data Engineering & Feature Processing</h4>
    <p>
        Data ingestion, missing value imputation, and feature engineering deriving <code>Customer_Engagement</code>, 
        <code>Revenue_Per_Month</code>, and <code>Average_Call_Duration</code>.
    </p>
</div>

<div class="custom-card">
    <h4>2. Predictive Machine Learning Engine</h4>
    <p>
        Evaluated 5 classification algorithms (Random Forest, XGBoost, Decision Tree, Gradient Boosting, Logistic Regression). 
        Selected <b>XGBoost Classifier</b> achieving <b>94.04% Accuracy</b> and <b>97.31% ROC-AUC</b> score.
    </p>
</div>

<div class="custom-card">
    <h4>3. Production REST API Microservice</h4>
    <p>
        FastAPI microservice offering real-time prediction endpoints (<code>POST /predict</code> and <code>POST /predict_batch</code>) 
        with Pydantic request payload validation.
    </p>
</div>

<div class="custom-card">
    <h4>4. Executive Dashboard & Analytical UI</h4>
    <p>
        Multi-page Streamlit application providing interactive KPI tracking, real-time risk scoring, 
        batch CSV processing, SQL analytics console, and retention ROI modeling.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.caption("Customer Churn Intelligence Platform | Engineering Documentation")
