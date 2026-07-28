<div align="center">

# 📊 Customer Churn Intelligence & Analytics Platform

**An enterprise-grade, end-to-end Machine Learning, SQL Analytics, and MLOps solution** that predicts telecommunications customer churn, identifies high-risk accounts, and quantifies retention campaign ROI.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.6+-111111?style=flat-square)](https://xgboost.readthedocs.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Accuracy](https://img.shields.io/badge/Accuracy-94.04%25-10B981?style=flat-square)]()
[![ROC--AUC](https://img.shields.io/badge/ROC--AUC-97.31%25-4F46E5?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

[Live App](https://customer-churn-prediction-dquj8ttzoyx9l2q3tzsd59.streamlit.app/) · [API Docs](https://customer-churn-prediction-70xe.onrender.com/docs) · [Power BI Dashboard](powerbi/Customer_Churn_Dashboard.pbix) · [Quick Start](#-quick-start--local-setup)

</div>

<br>

## 📑 Table of Contents

- [Live Deployments](#-live-deployments--api-documentation)
- [Application Screenshots](#️-application-screenshots)
- [Key Capabilities](#-key-system-capabilities)
- [Model Comparison](#-machine-learning-model-comparison)
- [System Architecture](#️-system-architecture--workflow-pipeline)
- [Repository Structure](#-project-repository-structure)
- [Quick Start](#-quick-start--local-setup)
- [Business Recommendations](#-business-key-recommendations)
- [License](#-license)

<br>

## 🔗 Live Deployments & API Documentation

| Resource | Link |
| :--- | :--- |
| 🚀 **Live Web Application** | [customer-churn-prediction.streamlit.app](https://customer-churn-prediction-dquj8ttzoyx9l2q3tzsd59.streamlit.app/) |
| ⚡ **Production REST API Docs** | [customer-churn-api.onrender.com/docs](https://customer-churn-prediction-70xe.onrender.com/docs) |
| 📊 **Power BI Dashboard** | [powerbi/Customer_Churn_Dashboard.pbix](powerbi/Customer_Churn_Dashboard.pbix) |

<br>

## 🖼️ Application Screenshots

### 1️⃣ Executive Dashboard & Portfolio Analytics
> Interactive KPI metrics, tenure cohort churn distribution, complaint history breakdown, and portfolio filters.

<p align="center">
  <img width="48%" alt="dashboard_preview_1" src="https://github.com/user-attachments/assets/d89c5eca-5052-462a-81fa-dcd7e9fc2be1" />
  &nbsp;
  <img width="48%" alt="dashboard_preview_2" src="https://github.com/user-attachments/assets/b957fe66-02e1-4ccf-9229-136f95060111" />
</p>

### 2️⃣ Real-Time Churn Predictor & Explainable AI (XAI)
> Single customer risk evaluation, probability gauge dial, and per-feature influence breakdown.

<p align="center">
  <img width="48%" alt="predictor_preview_1" src="https://github.com/user-attachments/assets/33f6de85-b757-475e-b99f-7f4505c0ea3a" />
  &nbsp;
  <img width="48%" alt="predictor_preview_2" src="https://github.com/user-attachments/assets/b1482208-fd47-46b3-954b-5904476f7004" />
</p>

### 3️⃣ Batch CSV Risk Dataset Processing
> Bulk upload customer datasets, generate risk score predictions, and download processed CSV reports.

<p align="center">
  <img width="48%" alt="batch_preview_1" src="https://github.com/user-attachments/assets/1b1861e1-78c0-4a76-a74f-5f4868b99c16" />
  &nbsp;
  <img width="48%" alt="batch_preview_2" src="https://github.com/user-attachments/assets/84c10fcc-07a2-4df7-b096-a0bdd91848a6" />
</p>

### 4️⃣ Production REST API Microservice (FastAPI & Swagger UI)
> High-performance asynchronous prediction endpoints (`POST /predict` and `POST /predict_batch`).

<p align="center">
  <img width="70%" alt="api_docs_preview" src="https://github.com/user-attachments/assets/3e13cb55-a201-4b2e-a629-dc49b7151c4c" />
</p>

<br>

## 🎯 Key System Capabilities

| Capability | Description |
| :--- | :--- |
| 🔮 **Real-Time Risk Classification** | Instant risk tier assignment (Low / Medium / High) powered by an **XGBoost Classifier** |
| 📦 **Batch Dataset Processing** | Upload customer CSV files, calculate bulk risk scores, and export processed CSV outputs |
| 🧠 **Explainable AI (XAI)** | Feature contribution breakdown identifying key risk drivers per customer |
| 🗃️ **SQL Analytics Studio** | Query console connected to SQLite database storage (`sql/churn.db`) |
| 💰 **Retention Campaign ROI Calculator** | Financial simulator estimating gross revenue preserved vs. campaign costs |
| ⚙️ **MLOps Pipeline** | Automated **Pytest** testing suite & **GitHub Actions CI/CD** workflow |

<br>

## 🏆 Machine Learning Model Comparison

Evaluated **5 classification algorithms** on the UCI Telecom Customer Churn Dataset (2,850 records):

<p align="center">
  <img width="90%" alt="model_comparison" src="https://github.com/user-attachments/assets/dcd5b5a1-ee65-4a07-81f7-a8ecc130585a" />
</p>

| Model Algorithm | Accuracy | Precision | Recall | F1 Score | ROC-AUC | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **XGBoost Classifier** | **94.04%** | **85.50%** | **76.00%** | **0.8048** | **97.31%** | 🏆 Selected |
| Random Forest Classifier | 94.04% | 86.67% | 75.28% | 0.7929 | 97.31% | Benchmark |
| Gradient Boosting | 93.16% | 84.00% | 74.00% | 0.7865 | 96.10% | Benchmark |
| Decision Tree | 92.10% | 81.00% | 72.00% | 0.7623 | 90.50% | Benchmark |
| Logistic Regression | 90.94% | 78.00% | 68.00% | 0.7267 | 88.20% | Baseline |

<br>

## 🏗️ System Architecture & Workflow Pipeline

<p align="center">
  <img width="90%" alt="architecture_diagram" src="https://github.com/user-attachments/assets/a3f7cfa3-ed9e-4c6a-9d5a-22f3dcc20e8b" />
</p>

<br>

## 📂 Project Repository Structure

```text
Customer-Churn-Prediction/
├── 📁 .github/workflows/     # CI/CD — GitHub Actions automated pipeline
├── 📁 api/                   # Production FastAPI REST microservice
│   ├── main.py                 # API endpoints (POST /predict, POST /predict_batch)
│   └── schemas.py               # Pydantic payload validation models
├── 📁 data/                  # Raw, processed, and sample datasets
│   ├── sample_batch_customers.csv
│   └── 📁 processed/
├── 📁 models/                # Serialized XGBoost model artifact (.pkl)
├── 📁 notebooks/             # 9 end-to-end data science & modeling notebooks
├── 📁 powerbi/               # Power BI report file (.pbix) & screenshots
├── 📁 sql/                   # SQLite database (churn.db) & analytical queries
├── 📁 streamlit/             # Enterprise multi-page web application
│   ├── Home.py                  # Application entrypoint
│   ├── 📁 pages/                 # Dashboard, Predictor, Insights, SQL, ROI, About
│   └── 📁 utils/                 # Custom CSS, Plotly charts, DB & prediction helpers
├── 📁 tests/                 # Automated Pytest suite (preprocessing, model, DB)
├── 📄 requirements.txt       # Root dependency specifications
└── 📄 README.md              # Documentation
```

<br>

## 💻 Quick Start & Local Setup

**1. Clone the repository & set up a virtual environment**
```bash
git clone https://github.com/Shub-ways/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit web application**
```bash
streamlit run streamlit/Home.py
```
> Open your browser at `http://localhost:8501`

**4. Run the FastAPI production REST microservice**
```bash
uvicorn api.main:app --reload
```
> View the interactive Swagger API docs at `http://127.0.0.1:8000/docs`

**5. Run the automated test suite**
```bash
python -m pytest tests/
```

<br>

## 📌 Business Key Recommendations

1. **Rapid Complaint Escalation** — Unresolved customer complaints represent the single highest predictor of churn risk. Automated SLA alerts within 24 hours are critical.
2. **Inactivity Interventions** — Customer inactivity (`Status = 2`) precedes churn by 30–60 days. Re-engagement campaigns should trigger when usage drops below baseline.
3. **High-Value VIP Protection** — Dedicated loyalty reward tiers for the top 15% value customers yield maximum financial ROI.

<br>

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

<div align="center">

---
Made with ⚙️ XGBoost · 🎈 Streamlit · ⚡ FastAPI

</div>
