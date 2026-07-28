import streamlit as st
import pandas as pd
from pathlib import Path

@st.cache_data
def load_dataset():
    base_dir = Path(__file__).resolve().parents[2]
    file_path = base_dir / "data" / "processed" / "churn_processed.csv"

    return pd.read_csv(file_path)