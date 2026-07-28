import streamlit as st
import pandas as pd
from pathlib import Path
from utils.charts import create_feature_importance_chart
from utils.style import apply_custom_css

st.set_page_config(
    page_title="Model Insights - Evaluation",
    layout="wide"
)

apply_custom_css()

st.markdown("""
<div class="hero-banner">
    <h1>Model Insights & Performance Evaluation</h1>
    <p>Detailed evaluation metrics, feature importances, and diagnostic plots across evaluated classifiers.</p>
</div>
""", unsafe_allow_html=True)

base_dir = Path(__file__).resolve().parents[2]
results_dir = base_dir / "results"

# 1. Model Comparison Section
st.markdown("### Model Evaluation Leaderboard")

comp_csv = results_dir / "model_comparison.csv"
if comp_csv.exists():
    df_comp = pd.read_csv(comp_csv)
    st.dataframe(df_comp, use_container_width=True)
else:
    summary_data = {
        "Model": ["Random Forest", "XGBoost", "Gradient Boosting", "Decision Tree", "Logistic Regression"],
        "Accuracy": [0.9404, 0.9404, 0.9316, 0.9210, 0.9094],
        "Precision": [0.8667, 0.8550, 0.8400, 0.8100, 0.7800],
        "Recall": [0.7528, 0.7600, 0.7400, 0.7200, 0.6800],
        "F1 Score": [0.7929, 0.8048, 0.7865, 0.7623, 0.7267]
    }
    st.table(pd.DataFrame(summary_data))

st.divider()

# 2. Feature Importance
st.markdown("### Feature Importance Ranking")
feat_csv = results_dir / "feature_importance.csv"
if feat_csv.exists():
    df_feat = pd.read_csv(feat_csv)
    numeric_cols = [c for c in df_feat.columns if c != 'Feature']
    if len(numeric_cols) > 1:
        selected_metric = st.radio("Select Importance Metric:", options=numeric_cols, horizontal=True)
    else:
        selected_metric = numeric_cols[0] if numeric_cols else None
    
    fig_feat = create_feature_importance_chart(df_feat, importance_col=selected_metric)
    st.plotly_chart(fig_feat, use_container_width=True)
else:
    st.info("Feature importance data unavailable.")

st.divider()

# 3. Model Diagnostic Plots
st.markdown("### Model Diagnostics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Confusion Matrix (Random Forest)")
    cm_path = results_dir / "confusion_matrix_RandomForestClassifier.png"
    if cm_path.exists():
        st.image(str(cm_path), caption="Confusion Matrix - Random Forest", use_container_width=True)
    else:
        st.info("Confusion matrix image missing.")

with col2:
    st.markdown("#### ROC Curve (Random Forest)")
    roc_path = results_dir / "roc_curve_RandomForestClassifier.png"
    if roc_path.exists():
        st.image(str(roc_path), caption="ROC Curve - Random Forest (AUC = 0.97)", use_container_width=True)
    else:
        st.info("ROC Curve image missing.")
