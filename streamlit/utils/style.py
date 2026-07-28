import streamlit as st

def apply_custom_css():
    """
    Applies an executive-grade dashboard layout:
    - Soft Slate Canvas background (#F1F5F9)
    - Crisp White Cards (#FFFFFF) with 1px border (#CBD5E1) and subtle drop shadow
    - Dark Slate Hero Header Banner for immediate visual contrast and depth
    - CSS rule renaming default 'app' sidebar navigation text to 'Home'
    """
    st.markdown("""
    <style>
        /* Import Google Font Inter */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            color: #0F172A;
        }

        /* Page Canvas Background */
        .stApp {
            background-color: #F1F5F9 !important;
        }

        /* Main Container Padding */
        .main .block-container {
            padding-top: 1.5rem;
            padding-bottom: 3rem;
            max-width: 1250px;
        }

        /* Executive Hero Header Banner */
        .hero-banner {
            background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
            border-radius: 10px;
            padding: 24px 30px;
            margin-bottom: 24px;
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
            border-left: 5px solid #4F46E5;
        }

        .hero-banner h1 {
            color: #FFFFFF !important;
            font-weight: 800 !important;
            font-size: 2.1rem !important;
            letter-spacing: -0.02em !important;
            margin: 0 0 6px 0 !important;
        }

        .hero-banner p {
            color: #94A3B8 !important;
            font-size: 0.98rem !important;
            margin: 0 !important;
            font-weight: 400 !important;
        }

        /* High-Contrast Section Headers */
        h2, h3 {
            color: #0F172A !important;
            font-weight: 700 !important;
            letter-spacing: -0.01em !important;
        }

        h4, h5 {
            color: #1E293B !important;
            font-weight: 600 !important;
        }

        /* Sidebar Styling & Nav Text Fix (Renaming 'app' -> 'Home') */
        section[data-testid="stSidebar"] {
            background-color: #E2E8F0 !important;
            border-right: 1px solid #CBD5E1 !important;
        }

        section[data-testid="stSidebar"] * {
            color: #0F172A !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid #94A3B8 !important;
            color: #0F172A !important;
        }

        /* Rename default 'app' link to 'Home' in sidebar nav */
        div[data-testid="stSidebarNav"] li:first-child span {
            visibility: hidden;
            position: relative;
        }

        div[data-testid="stSidebarNav"] li:first-child span::after {
            content: "Home";
            visibility: visible;
            position: absolute;
            left: 0;
            top: 0;
            font-weight: 600;
            color: #0F172A;
        }

        /* Pure White Elevated Metric Cards */
        [data-testid="stMetric"] {
            background-color: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            border-top: 3px solid #4F46E5 !important;
            border-radius: 8px !important;
            padding: 14px 18px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
        }

        [data-testid="stMetricValue"] {
            font-weight: 800 !important;
            color: #0F172A !important;
            font-size: 1.65rem !important;
        }

        [data-testid="stMetricLabel"] {
            font-weight: 600 !important;
            color: #475569 !important;
            font-size: 0.82rem !important;
            text-transform: uppercase !important;
            letter-spacing: 0.04em !important;
        }

        /* Pure White Elevated Content Cards */
        .custom-card, .info-card {
            background-color: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-top: 3px solid #4F46E5;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 18px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        }

        .custom-card h4, .info-card h4 {
            margin-top: 0;
            margin-bottom: 8px;
            color: #0F172A;
            font-size: 1.1rem;
            font-weight: 700;
        }

        .custom-card p, .info-card p {
            margin: 0;
            color: #334155;
            font-size: 0.92rem;
            line-height: 1.55;
        }

        /* Fixed Height Module Cards */
        .module-card {
            background-color: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-top: 3px solid #4F46E5;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 18px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            min-height: 165px;
            box-sizing: border-box;
        }

        .module-card h4 {
            margin-top: 0;
            margin-bottom: 8px;
            color: #0F172A;
            font-size: 1.1rem;
            font-weight: 700;
        }

        .module-card p {
            margin: 0;
            color: #334155;
            font-size: 0.92rem;
            line-height: 1.5;
        }

        /* Fixed Height Equal Cards for Multi-Column Layouts */
        .equal-card {
            background-color: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-top: 3px solid #4F46E5;
            border-radius: 8px;
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            min-height: 250px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .equal-card h4 {
            margin-top: 0;
            margin-bottom: 10px;
            color: #0F172A;
            font-size: 1.1rem;
            font-weight: 700;
        }

        .equal-card p {
            margin: 0;
            color: #334155;
            font-size: 0.92rem;
            line-height: 1.55;
        }

        /* High-Contrast Badges */
        .badge {
            display: inline-block;
            padding: 4px 10px;
            font-size: 0.75rem;
            font-weight: 700;
            border-radius: 4px;
            text-transform: uppercase;
        }
        .badge-success { background-color: #DCFCE7; color: #15803D; border: 1px solid #86EFAC; }
        .badge-warning { background-color: #FEF3C7; color: #B45309; border: 1px solid #FDE68A; }
        .badge-danger { background-color: #FEE2E2; color: #B91C1C; border: 1px solid #FCA5A5; }
        .badge-info { background-color: #E0F2FE; color: #0369A1; border: 1px solid #7DD3FC; }

        /* Form Buttons */
        div.stButton > button[kind="primary"] {
            background-color: #4F46E5 !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
            border: 1px solid #4338CA !important;
            border-radius: 6px !important;
            padding: 0.55rem 1.6rem !important;
            box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2) !important;
        }

        div.stButton > button[kind="primary"]:hover {
            background-color: #4338CA !important;
        }
    </style>
    """, unsafe_allow_html=True)
