import streamlit as st
from utils.style import apply_custom_css

st.set_page_config(
    page_title="Customer Churn Intelligence Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

st.title("Customer Churn Intelligence Platform")
st.markdown("##### *Predictive Analytics, Customer Risk Scoring, and Strategic Retention Insights*")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Platform Overview")
    st.write("""
    The **Customer Churn Intelligence Platform** is an enterprise-grade analytics application 
    designed to identify high-risk customer segments, predict individual churn probabilities 
    using Machine Learning, and provide actionable business recommendations to optimize retention.
    """)
    st.info("Navigate through the application using the sidebar menu.")

with col2:
    st.markdown("### Core Capabilities")
    st.markdown("""
    - **Executive Dashboard**: Interactive KPI tracking and customer segment filtering.
    - **Real-Time Prediction**: Instant risk classification powered by an XGBoost predictive model.
    - **Model Evaluation**: Diagnostic metrics, feature importance rankings, and ROC curves.
    - **SQL Analytics Studio**: Query engine connected directly to customer dataset storage.
    - **Retention ROI Calculator**: Strategic campaign financial simulation.
    """)

st.divider()

st.caption("Customer Churn Prediction Project | Production Release")