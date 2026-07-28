import streamlit as st
from utils.load_data import load_dataset
from utils.style import apply_custom_css

st.set_page_config(
    page_title="Home - Customer Churn Intelligence",
    layout="wide"
)

apply_custom_css()

st.markdown("""
<div class="hero-banner">
    <h1>Executive Overview</h1>
    <p>Key retention performance metrics and system capabilities.</p>
</div>
""", unsafe_allow_html=True)

# High-Level Metrics Summary
df = load_dataset()
total_customers = len(df)
total_churned = int(df['Churn'].sum())
churn_rate = (total_churned / total_customers) * 100
avg_val = df['Customer Value'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Active Portfolio", f"{total_customers:,}")
col2.metric("Total Churned Customers", f"{total_churned:,}")
col3.metric("Portfolio Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Average Customer Value", f"${avg_val:.2f}")

st.divider()

st.markdown("### Application Modules")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
    <div class="module-card">
        <h4>Executive Dashboard</h4>
        <p>
            Real-time metric monitoring, age cohort analysis, tariff plan breakdowns, and interactive customer filtering.
        </p>
    </div>
    <div class="module-card">
        <h4>Real-Time Churn Predictor</h4>
        <p>
            Enter customer behavioral profile data to calculate instant churn probabilities and risk tier classifications.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="module-card">
        <h4>Model Diagnostics & Insights</h4>
        <p>
            Review machine learning model evaluations, feature importance rankings, confusion matrices, and ROC curves.
        </p>
    </div>
    <div class="module-card">
        <h4>SQL Analytics Studio</h4>
        <p>
            Execute analytical SQL queries directly against the database to generate custom business intelligence reports.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("### Strategic Highlights")
st.markdown("""
- **Complaint Resolution Impact**: Unresolved customer complaints represent the single highest predictor of churn risk.
- **Inactivity Risk**: Customers entering an inactive status require immediate re-engagement within 30 days.
- **Tenure Protection**: Early tenure customers (0–12 months) show elevated sensitivity to service friction.
""")