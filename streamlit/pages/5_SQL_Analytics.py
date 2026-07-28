import streamlit as st
from utils.database import run_query
from utils.style import apply_custom_css

st.set_page_config(
    page_title="SQL Analytics - Business Queries",
    layout="wide"
)

apply_custom_css()

st.markdown("""
<div class="hero-banner">
    <h1>SQL Analytics Studio</h1>
    <p>Execute predefined business intelligence queries or custom SQL statements against SQLite database storage.</p>
</div>
""", unsafe_allow_html=True)

PRESET_QUERIES = {
    "Overall Churn Summary": """SELECT 
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    COUNT(*) - SUM(Churn) AS retained_customers,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_percentage
FROM customers;""",

    "Churn Rate by Customer Status": """SELECT 
    CASE Status 
        WHEN 1 THEN 'Active'
        WHEN 2 THEN 'Inactive'
        ELSE 'Unknown'
    END AS status_label,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_percentage
FROM customers
GROUP BY Status;""",

    "Churn Risk by Complaint History": """SELECT 
    CASE Complains 
        WHEN 0 THEN 'No Complaints'
        WHEN 1 THEN 'Has Complained'
    END AS complaint_status,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers,
    ROUND(AVG(Churn) * 100, 2) AS churn_rate_percentage
FROM customers
GROUP BY Complains;""",

    "Average Usage Metrics by Status": """SELECT 
    CASE Churn 
        WHEN 1 THEN 'Churned'
        ELSE 'Retained'
    END AS churn_status,
    ROUND(AVG("Seconds of Use"), 2) AS avg_seconds_of_use,
    ROUND(AVG("Frequency of use"), 2) AS avg_frequency_of_use,
    ROUND(AVG("Distinct Called Numbers"), 2) AS avg_distinct_calls,
    ROUND(AVG("Customer Value"), 2) AS avg_customer_value
FROM customers
GROUP BY Churn;""",

    "High-Value At-Risk Customers": """SELECT 
    "Subscription Length",
    "Customer Value",
    "Revenue_Per_Month",
    "Complains",
    "Status",
    "Frequency of use"
FROM customers
WHERE Churn = 1 AND "Customer Value" > (SELECT AVG("Customer Value") FROM customers)
ORDER BY "Customer Value" DESC
LIMIT 10;"""
}

st.markdown("### Preset Analytical Queries")
selected_preset = st.selectbox("Select a SQL Preset Query:", options=list(PRESET_QUERIES.keys()))

user_query = st.text_area(
    "SQL Query Console:",
    value=PRESET_QUERIES[selected_preset],
    height=170
)

if st.button("Execute Query", type="primary"):
    if not user_query.strip():
        st.warning("Please enter a SQL query.")
    else:
        try:
            df_result = run_query(user_query)
            st.success(f"Query executed successfully ({len(df_result)} rows returned).")
            st.dataframe(df_result, use_container_width=True)
        except Exception as e:
            st.error(f"SQL Execution Error: {e}")
