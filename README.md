# Customer Churn Intelligence & Analytics Platform

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.6+-111111?style=flat-square)](https://xgboost.readthedocs.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Accuracy](https://img.shields.io/badge/Accuracy-94.04%25-10B981?style=flat-square)]()
[![ROC--AUC](https://img.shields.io/badge/ROC--AUC-97.31%25-4F46E5?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

An enterprise-grade, end-to-end Machine Learning, SQL Analytics, and MLOps solution designed to predict telecommunications customer churn, identify high-risk accounts, and evaluate retention campaign financial ROI.

---

## 🔗 Live Deployments & API Documentation

- **🚀 Live Web Application**: [https://customer-churn-prediction.streamlit.app](https://customer-churn-prediction.streamlit.app)
- **⚡ Production REST API Docs**: [https://customer-churn-api.onrender.com/docs](https://customer-churn-api.onrender.com/docs)
- **📊 Power BI Dashboard**: [powerbi/Customer_Churn_Dashboard.pbix](file:///d:/Projects/Customer-Churn-Prediction/powerbi/Customer_Churn_Dashboard.pbix)

---

## 🖼️ Application Screenshots

### 1. Executive Dashboard & Portfolio Analytics
> *Interactive KPI metrics, tenure cohort churn distribution, complaint history breakdown, and portfolio filters.*

![Executive Dashboard Preview](streamlit/assets/dashboard_preview.png)

---

### 2. Real-Time Churn Predictor & Explainable AI (XAI)
> *Single customer risk evaluation, probability gauge dial, and per-feature influence breakdown.*

![Predictor & Feature Influence Preview](streamlit/assets/predictor_preview.png)

---

### 3. Batch CSV Risk Dataset Processing
> *Bulk upload customer datasets, generate risk score predictions, and download processed CSV reports.*

![Batch Processing Preview](streamlit/assets/batch_preview.png)

---

### 4. Production REST API Microservice (FastAPI & Swagger UI)
> *High-performance asynchronous prediction endpoints (`POST /predict` and `POST /predict_batch`).*

![FastAPI Swagger UI Preview](streamlit/assets/api_docs_preview.png)

---

## 🎯 Key System Capabilities

* **Real-Time Risk Classification**: Instant risk tier assignment (Low, Medium, High Risk) powered by an **XGBoost Classifier**.
* **Batch Dataset Processing**: Upload customer CSV files, calculate bulk risk scores, and export processed CSV outputs.
* **Explainable AI (XAI)**: Feature contribution breakdown identifying key risk drivers per customer.
* **SQL Analytics Studio**: Query console connected to SQLite database storage (`sql/churn.db`).
* **Retention Campaign ROI Calculator**: Financial simulator estimating gross revenue preserved vs campaign costs.
* **MLOps Pipeline**: Automated **Pytest** testing suite & **GitHub Actions CI/CD** workflow.

---

## 🏆 Machine Learning Model Comparison

Evaluated 5 classification algorithms on the **UCI Telecom Customer Churn Dataset** (2,850 records):

| Model Algorithm | Accuracy | Precision | Recall | F1 Score | ROC-AUC | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **XGBoost Classifier** | **94.04%** | **85.50%** | **76.00%** | **0.8048** | **97.31%** | 🏆 Selected |
| **Random Forest Classifier** | **94.04%** | 86.67% | 75.28% | 0.7929 | 97.31% | Benchmark |
| **Gradient Boosting** | 93.16% | 84.00% | 74.00% | 0.7865 | 96.10% | Benchmark |
| **Decision Tree** | 92.10% | 81.00% | 72.00% | 0.7623 | 90.50% | Benchmark |
| **Logistic Regression** | 90.94% | 78.00% | 68.00% | 0.7267 | 88.20% | Baseline |

---

## 🏗️ System Architecture & Workflow Pipeline

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│ Raw Data Ingest │ ---> │ Data Prep & XAI  │ ---> │ XGBoost Model   │
│ (UCI Repository)│      │ Feature Deriv.   │      │ (Accuracy 94%)  │
└─────────────────┘      └──────────────────┘      └────────┬────────┘
                                                            │
    ┌───────────────────────────────────────────────────────┴───────────────────────────────────────────────────────┐
    │                                                       │                                                       │
    ▼                                                       ▼                                                       ▼
┌────────────────────────┐              ┌────────────────────────┐              ┌────────────────────────┐
│ Streamlit UI Platform  │              │ SQLite Database Storage│              │ FastAPI REST Service   │
│ Multi-Page Analytics   │              │ (sql/churn.db)         │              │ (POST /predict)        │
└────────────────────────┘              └────────────────────────┘              └────────────────────────┘
```

---

## 📂 Project Repository Structure

```
Customer-Churn-Prediction/
├── 📁 .github/workflows/    # GitHub Actions Automated CI Pipeline
├── 📁 api/                  # Production FastAPI REST Microservice
│   ├── main.py              # API Endpoints (POST /predict, POST /predict_batch)
│   └── schemas.py           # Pydantic Payload Validation Models
├── 📁 data/                 # Raw, Processed, and Sample Datasets
│   ├── sample_batch_customers.csv
│   └── processed/
├── 📁 models/                # Serialized XGBoost Model Artifact (.pkl)
├── 📁 notebooks/             # 9 End-to-End Data Science & Modeling Notebooks
├── 📁 powerbi/               # Power BI Report File (.pbix) & Screenshots
├── 📁 sql/                   # SQLite Database (churn.db) & Analytical Queries
├── 📁 streamlit/             # Enterprise Multi-Page Web Application
│   ├── Home.py              # Application Entrypoint
│   ├── 📁 pages/            # Dashboard, Predictor, Insights, SQL, ROI, About
│   └── 📁 utils/            # Custom CSS, Plotly Charts, Database & Prediction Helpers
├── 📁 tests/                # Automated Pytest Suite (Preprocessing, Model, DB)
├── 📄 requirements.txt      # Root Dependency Specifications
└── 📄 README.md              # Documentation
```

---

## 💻 Quick Start & Local Setup

### 1. Clone Repository & Setup Virtual Environment
```bash
git clone https://github.com/Shub-ways/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Streamlit Web Application
```bash
streamlit run streamlit/Home.py
```
> Open browser at: `http://localhost:8501`

### 4. Run FastAPI Production REST Microservice
```bash
uvicorn api.main:app --reload
```
> View Interactive Swagger API Documentation at: `http://127.0.0.1:8000/docs`

### 5. Run Automated Test Suite
```bash
python -m pytest tests/
```

---

## 📌 Business Key Recommendations

1. **Rapid Complaint Escalation**: Unresolved customer complaints represent the single highest predictor of churn risk. Automated SLA alerts within 24 hours are critical.
2. **Inactivity Interventions**: Customer inactivity (`Status = 2`) precedes churn by 30 to 60 days. Re-engagement campaigns should trigger when usage drops below baseline.
3. **High-Value VIP Protection**: Dedicated loyalty reward tiers for top 15% value customers yield maximum financial ROI.

---

## 📄 License
Distributed under the MIT License. See [LICENSE](LICENSE) for details.