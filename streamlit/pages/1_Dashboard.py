import streamlit as st
from utils.load_data import load_dataset
from utils.style import apply_custom_css
from utils.charts import (
    create_churn_pie_chart,
    create_complaint_churn_chart,
    create_usage_scatter_chart,
    create_tenure_cohort_chart
)

st.set_page_config(
    page_title="Dashboard - Customer Churn Intelligence",
    layout="wide"
)

apply_custom_css()

df = load_dataset()

st.markdown("""
<div class="hero-banner">
    <h1>Executive Dashboard</h1>
    <p>Comprehensive analysis of customer churn metrics, usage behaviors, and segment breakdown.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Filters
st.sidebar.markdown("### Portfolio Filters")

age_groups = sorted(df["Age Group"].unique())
age_group = st.sidebar.multiselect("Age Group", options=age_groups, default=age_groups)

statuses = sorted(df["Status"].unique())
status = st.sidebar.multiselect("Status (1=Active, 2=Inactive)", options=statuses, default=statuses)

tariffs = sorted(df["Tariff Plan"].unique())
tariff = st.sidebar.multiselect("Tariff Plan", options=tariffs, default=tariffs)

filtered_df = df[
    (df["Age Group"].isin(age_group)) &
    (df["Status"].isin(status)) &
    (df["Tariff Plan"].isin(tariff))
]

if filtered_df.empty:
    st.warning("No data matches the selected filters. Please broaden your selection.")
    st.stop()

# Key Performance Indicators
total_customers = len(filtered_df)
churned_customers = filtered_df["Churn"].sum()
churn_rate = (churned_customers / total_customers * 100) if total_customers else 0
avg_customer_value = filtered_df["Customer Value"].mean()
total_complaints = filtered_df["Complains"].sum()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Count", f"{int(churned_customers):,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")
col4.metric("Avg Customer Value", f"${avg_customer_value:.2f}")
col5.metric("Total Complaints", f"{int(total_complaints):,}")

st.divider()

# Charts Grid
tab1, tab2 = st.columns(2)

with tab1:
    fig_pie = create_churn_pie_chart(filtered_df)
    st.plotly_chart(fig_pie, use_container_width=True)

with tab2:
    fig_comp = create_complaint_churn_chart(filtered_df)
    st.plotly_chart(fig_comp, use_container_width=True)

st.divider()

tab3, tab4 = st.columns(2)

with tab3:
    fig_scatter = create_usage_scatter_chart(filtered_df)
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab4:
    fig_tenure = create_tenure_cohort_chart(filtered_df)
    st.plotly_chart(fig_tenure, use_container_width=True)

# Filtered Table View
with st.expander("View Filtered Data Table"):
    st.dataframe(filtered_df.head(100), use_container_width=True)