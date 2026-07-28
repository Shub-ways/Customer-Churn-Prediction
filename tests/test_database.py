import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(base_dir / "streamlit"))

from utils.database import run_query, get_all_customers

def test_run_query():
    df = run_query("SELECT COUNT(*) AS total FROM customers")
    assert len(df) == 1
    assert df.iloc[0, 0] > 0

def test_get_all_customers():
    df = get_all_customers()
    assert len(df) >= 2850
    assert 'Churn' in df.columns
