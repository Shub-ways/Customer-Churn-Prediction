import streamlit as st
import pandas as pd
from pathlib import Path
from utils.preprocessing import format_prediction_input
from utils.prediction import predict_churn, batch_predict_churn, get_feature_contributions
from utils.charts import create_gauge_chart, create_feature_contribution_chart
from utils.style import apply_custom_css

st.set_page_config(
    page_title="Predict Churn - Machine Learning Tool",
    layout="wide"
)

apply_custom_css()

st.markdown("""
<div class="hero-banner">
    <h1>Real-Time Churn Risk Predictor</h1>
    <p>Calculate instant churn risk scores for individual customers or process batch CSV datasets.</p>
</div>
""", unsafe_allow_html=True)

tab_single, tab_batch = st.tabs(["Single Customer Risk Assessment", "Batch CSV Risk Processing"])

# TAB 1: Single Customer Prediction
with tab_single:
    with st.form("churn_prediction_form"):
        st.markdown("### Customer Parameters & Usage Metrics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            subscription_length = st.number_input("Subscription Length (Months)", min_value=1, max_value=60, value=38)
            frequency_of_use = st.number_input("Frequency of Use (Calls)", min_value=0, max_value=500, value=71)
            seconds_of_use = st.number_input("Seconds of Use (Total Duration)", min_value=0, max_value=25000, value=4370)
            
        with col2:
            distinct_called_numbers = st.number_input("Distinct Called Numbers", min_value=0, max_value=150, value=17)
            frequency_of_sms = st.number_input("Frequency of SMS", min_value=0, max_value=1000, value=5)
            customer_value = st.number_input("Customer Value ($)", min_value=0.0, max_value=3000.0, value=197.64)

        with col3:
            status = st.selectbox("Account Status", options=[1, 2], format_func=lambda x: "Active" if x == 1 else "Inactive", index=0)
            complains = st.radio("Logged Complaint History", options=[0, 1], format_func=lambda x: "No Complaints Logged" if x == 0 else "Complaint Logged", index=0)
            
        submit_button = st.form_submit_button("Calculate Risk Score", type="primary")

    if submit_button:
        input_df = format_prediction_input(
            complains=complains,
            subscription_length=subscription_length,
            frequency_of_use=frequency_of_use,
            seconds_of_use=seconds_of_use,
            distinct_called_numbers=distinct_called_numbers,
            status=status,
            customer_value=customer_value,
            frequency_of_sms=frequency_of_sms
        )
        
        pred_class, probability, risk_tier = predict_churn(input_df)
        
        st.divider()
        st.markdown("### Risk Analysis Results")
        
        res_col1, res_col2 = st.columns([1, 1])
        
        with res_col1:
            fig_gauge = create_gauge_chart(probability)
            st.plotly_chart(fig_gauge, use_container_width=True)
            
        with res_col2:
            badge_class = "badge-danger" if risk_tier == "High Risk" else ("badge-warning" if risk_tier == "Medium Risk" else "badge-success")
            
            st.markdown(f"""
            <div class="custom-card">
                <h4>Risk Classification: <span class="badge {badge_class}">{risk_tier}</span></h4>
                <p style="font-size: 1.1rem; font-weight: 600; color: #0F172A; margin-top: 10px;">
                    Estimated Churn Probability: {probability * 100:.2f}%
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            if pred_class == 1:
                st.error("High risk of churn detected. Immediate intervention recommended.")
                st.markdown("""
                **Recommended Actions:**
                - Priority outreach by customer support team within 24 hours.
                - Provide targeted retention offer or plan optimization.
                - Expedite resolution of any logged complaints.
                """)
            else:
                st.success("Low churn probability. Customer profile indicates stable engagement.")
                st.markdown("""
                **Recommended Actions:**
                - Continue standard automated lifecycle communication.
                - Monitor account status during annual renewal window.
                """)

        st.divider()
        
        # Feature Contribution Breakdown
        df_contrib = get_feature_contributions(input_df)
        fig_contrib = create_feature_contribution_chart(df_contrib)
        st.plotly_chart(fig_contrib, use_container_width=True)

# TAB 2: Batch CSV Processing
with tab_batch:
    st.markdown("### Upload Customer Data CSV for Bulk Prediction")
    st.caption("Upload a CSV dataset containing customer features to compute batch risk scores.")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            batch_df = pd.read_csv(uploaded_file)
            st.success(f"File uploaded successfully ({len(batch_df)} records).")
            
            if st.button("Process Batch Predictions", type="primary"):
                processed_df = batch_predict_churn(batch_df)
                
                st.markdown("#### Batch Prediction Summary Results")
                
                sum_col1, sum_col2, sum_col3 = st.columns(3)
                high_count = (processed_df['Risk_Tier'] == 'High Risk').sum()
                med_count = (processed_df['Risk_Tier'] == 'Medium Risk').sum()
                low_count = (processed_df['Risk_Tier'] == 'Low Risk').sum()
                
                sum_col1.metric("High Risk Accounts", f"{high_count:,}")
                sum_col2.metric("Medium Risk Accounts", f"{med_count:,}")
                sum_col3.metric("Low Risk Accounts", f"{low_count:,}")
                
                st.dataframe(processed_df, use_container_width=True)
                
                # Download CSV
                csv_bytes = processed_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Batch Predictions CSV",
                    data=csv_bytes,
                    file_name="churn_predictions_batch.csv",
                    mime="text/csv",
                    type="primary"
                )
        except Exception as e:
            st.error(f"Error processing CSV file: {e}")
    else:
        st.info("Upload a CSV file with columns matching the dataset (Complains, Subscription Length, Seconds of Use, etc.).")
        
        # Provide sample CSV template for quick testing
        sample_path = Path(__file__).resolve().parents[2] / "data" / "sample_batch_customers.csv"
        if sample_path.exists():
            sample_bytes = sample_path.read_bytes()
            st.download_button(
                label="📄 Download Sample Batch CSV Template",
                data=sample_bytes,
                file_name="sample_batch_customers.csv",
                mime="text/csv"
            )
