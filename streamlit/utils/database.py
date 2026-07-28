import sqlite3
import pandas as pd
from pathlib import Path

def get_db_connection():
    base_dir = Path(__file__).resolve().parents[2]
    db_path = base_dir / "sql" / "churn.db"
    return sqlite3.connect(db_path)

def run_query(query: str) -> pd.DataFrame:
    """
    Executes a SQL query against churn.db and returns a pandas DataFrame.
    """
    conn = get_db_connection()
    try:
        df = pd.read_sql_query(query, conn)
    finally:
        conn.close()
    return df

def get_all_customers() -> pd.DataFrame:
    """
    Returns full customers table from SQLite database.
    """
    return run_query("SELECT * FROM customers")
