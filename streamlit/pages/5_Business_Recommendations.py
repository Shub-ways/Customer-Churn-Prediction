import streamlit as st
from utils.load_data import load_dataset
from utils.style import apply_custom_css

st.set_page_config(
    page_title="Business Recommendations",
    layout="wide"
)

apply_custom_css()

st.markdown("""
<div class="hero-banner">
    <h1>Strategic Business Recommendations</h1>
    <p>Actionable retention strategies and financial ROI calculator based on Machine Learning insights.</p>
</div>
""", unsafe_allow_html=True)

# Core Strategic Pillars
st.markdown("### Strategic Pillars for Churn Prevention")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="equal-card">
        <div>
            <h4>1. Rapid Complaint Escalation</h4>
            <p>
                Unresolved complaints are the primary predictor of customer churn. 
                Implement automated SLA alerts for unresolved complaints within 24 hours.
            </p>
        </div>
        <div>
            <span class="badge badge-danger">High Priority</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="equal-card">
        <div>
            <h4>2. Early Inactivity Interventions</h4>
            <p>
                Customer inactivity precedes churn by 30 to 60 days. 
                Trigger automated re-engagement campaigns when usage drops below baseline.
            </p>
        </div>
        <div>
            <span class="badge badge-warning">Medium Priority</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="equal-card">
        <div>
            <h4>3. High-Value Customer VIP Care</h4>
            <p>
                Losing high-value accounts disproportionately impacts revenue. 
                Create dedicated loyalty reward tiers for top 15% value customers.
            </p>
        </div>
        <div>
            <span class="badge badge-info">Strategic Priority</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Interactive Retention Campaign ROI Calculator
st.markdown("### Retention Campaign Financial ROI Calculator")
st.caption("Simulate potential revenue preserved by running targeted retention campaigns on at-risk customers.")

df = load_dataset()
churned_df = df[df['Churn'] == 1]
total_churned_count = len(churned_df)
avg_churned_val = churned_df['Customer Value'].mean()

calc_col1, calc_col2 = st.columns([1, 1])

with calc_col1:
    target_percentage = st.slider("Targeted At-Risk Customers Saved (%)", min_value=5, max_value=50, value=20, step=5)
    campaign_cost_per_user = st.number_input("Campaign Incentive Cost per Customer ($)", min_value=1.0, max_value=100.0, value=15.0)

saved_customers = int(total_churned_count * (target_percentage / 100))
gross_revenue_saved = saved_customers * avg_churned_val
total_campaign_cost = total_churned_count * campaign_cost_per_user
net_benefit = gross_revenue_saved - total_campaign_cost
roi = (net_benefit / total_campaign_cost * 100) if total_campaign_cost > 0 else 0

with calc_col2:
    st.metric("Estimated Customers Retained", f"{saved_customers:,} users")
    st.metric("Gross Revenue Preserved", f"${gross_revenue_saved:,.2f}")
    st.metric("Net Campaign Financial Benefit", f"${net_benefit:,.2f}", delta=f"ROI: {roi:.1f}%")

st.divider()

st.info("Proactive, model-driven retention campaigns significantly outperform broad marketing by focusing resources exclusively on high-probability churn accounts.")
