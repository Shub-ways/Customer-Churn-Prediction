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

- **🚀 Live Web Application**: [https://customer-churn-prediction.streamlit.app](https://customer-churn-prediction-dquj8ttzoyx9l2q3tzsd59.streamlit.app/)
- **⚡ Production REST API Docs**: [https://customer-churn-api.onrender.com/docs]( https://customer-churn-prediction-70xe.onrender.com/docs)
- **📊 Power BI Dashboard**: [powerbi/Customer_Churn_Dashboard.pbix](file:///d:/Projects/Customer-Churn-Prediction/powerbi/Customer_Churn_Dashboard.pbix)

---

## 🖼️ Application Screenshots

### 1. Executive Dashboard & Portfolio Analytics
> *Interactive KPI metrics, tenure cohort churn distribution, complaint history breakdown, and portfolio filters.*

<img width="959" height="425" alt="dashboard_preview_1" src="https://github.com/user-attachments/assets/d89c5eca-5052-462a-81fa-dcd7e9fc2be1" />


<img width="959" height="451" alt="dashboard_preview_2" src="https://github.com/user-attachments/assets/b957fe66-02e1-4ccf-9229-136f95060111" />


---

### 2. Real-Time Churn Predictor & Explainable AI (XAI)
> *Single customer risk evaluation, probability gauge dial, and per-feature influence breakdown.*

<img width="959" height="419" alt="predictor_preview_1" src="https://github.com/user-attachments/assets/33f6de85-b757-475e-b99f-7f4505c0ea3a" />

<img width="959" height="423" alt="predictor_preview_2" src="https://github.com/user-attachments/assets/b1482208-fd47-46b3-954b-5904476f7004" />


---

### 3. Batch CSV Risk Dataset Processing
> *Bulk upload customer datasets, generate risk score predictions, and download processed CSV reports.*

<img width="959" height="323" alt="batch_preview_1" src="https://github.com/user-attachments/assets/1b1861e1-78c0-4a76-a74f-5f4868b99c16" />


<img width="959" height="430" alt="batch_preview_2" src="https://github.com/user-attachments/assets/84c10fcc-07a2-4df7-b096-a0bdd91848a6" />


---

### 4. Production REST API Microservice (FastAPI & Swagger UI)
> *High-performance asynchronous prediction endpoints (`POST /predict` and `POST /predict_batch`).*

<img width="959" height="381" alt="api_docs_preview" src="https://github.com/user-attachments/assets/3e13cb55-a201-4b2e-a629-dc49b7151c4c" />


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

<img width="2579" height="1379" alt="model_comparison" src="https://github.com/user-attachments/assets/dcd5b5a1-ee65-4a07-81f7-a8ecc130585a" />


---

## 🏗️ System Architecture & Workflow Pipeline


<img width="2779" height="1580" alt="architecture_diagram" src="https://github.com/user-attachments/assets/a3f7cfa3-ed9e-4c6a-9d5a-22f3dcc20e8b" />


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
