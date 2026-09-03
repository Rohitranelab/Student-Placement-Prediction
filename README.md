<div align="center">

# 🎓 Student Placement Prediction

### Predict whether a student will be placed — powered by an end-to-end MLOps pipeline with a live Flask web application.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-Benchmarked-EE4C2C?style=for-the-badge)](https://xgboost.readthedocs.io)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Demo](#-demo)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Workflow](#-workflow)
- [Dataset](#-dataset)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Data Preprocessing](#-data-preprocessing)
- [Models Used](#-models-used)
- [Model Performance](#-model-performance)
- [Installation](#-installation)
- [Usage](#-usage)
- [Example Predictions](#-example-predictions)
- [Visualizations](#-visualizations)
- [Configuration](#-configuration)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgements](#-acknowledgements)
- [Why This Project Stands Out](#-why-this-project-stands-out)

---

## 🔍 Project Overview

**Student Placement Prediction** is a production-ready machine learning application that predicts whether a student will receive a campus placement offer based on their academic profile, technical skills, soft skills, and interview performance.

**What problem does it solve?**
Campus placement drives are high-stakes events for students and institutions alike. Predicting placement outcomes in advance allows students to identify gaps and improve their profile, and enables training & placement cells to prioritise coaching resources.

**Why it matters:**
- Reduces student anxiety through data-driven self-assessment
- Enables career counsellors to intervene early for at-risk students
- Provides institutions with actionable insights on placement-readiness trends

**Real-world applications:**
- University placement cells and career services portals
- EdTech platforms offering personalised skill-gap analysis
- HR analytics tools to pre-screen campus candidates

**Expected users:** Students, career counsellors, training & placement officers, and HR professionals.

---

## 🎬 Demo

> **Live Application:** The Flask web app runs locally on `http://localhost:5000`.

| UI State | Preview |
|----------|---------|
| Prediction Form | ![UI Form](reports/figures/ui_form.png) |
| Result — Placed | ![Result Placed](reports/figures/result_placed.png) |
| Result — Not Placed | ![Result Not Placed](reports/figures/result_not_placed.png) |

> 📁 Screenshots are located in `reports/figures/`. Replace the paths above once figures are committed to the repository.

---

## ✅ Features

- [x] Automated data ingestion from a remote CSV source (GitHub-hosted dataset)
- [x] Schema-driven data validation with a JSON validation report
- [x] Data transformation with configurable column removal
- [x] Multi-model benchmarking across 9 classifiers in the research notebook
- [x] Production model training — Logistic Regression with configurable hyperparameters
- [x] Model evaluation with Accuracy, Precision, Recall & F1-score metrics saved to JSON
- [x] Trained model serialised with `pickle` for lightweight deployment
- [x] Flask web application with a clean, responsive HTML/CSS frontend
- [x] Structured logging throughout the entire pipeline
- [x] Custom exception handling with traceback context
- [x] YAML-based schema configuration for easy column management
- [x] Reproducible train/test split with a fixed random seed
- [x] Modular, component-based codebase following MLOps best practices
- [x] MIT-licensed open source project

---

## 🛠 Tech Stack

**Language**

| Tool | Version |
|------|---------|
| Python | 3.11 |

**Libraries & Frameworks**

| Library | Purpose |
|---------|---------|
| Pandas | Data loading, manipulation, and train/test split |
| Scikit-Learn | Model training, evaluation, and StandardScaler |
| XGBoost | Benchmarking (research notebook) |
| Flask | Web application server |
| PyYAML | Schema configuration file parsing |
| Pickle | Model serialisation |

**Visualization (Notebook)**

| Library | Purpose |
|---------|---------|
| Matplotlib | Plots and figures |
| Seaborn | Statistical visualisations (heatmap, countplots, histplots) |

**Project Tooling**

| Tool | Purpose |
|------|---------|
| `pyproject.toml` | Project metadata and packaging |
| `setup.sh` | Package setup script |
| Custom Logger | Structured timestamped logging to file |
| Custom Exception | Detailed exception messages with file and line context |

**Version Control**

| Tool |
|------|
| Git / GitHub |

---

## 📁 Project Structure

```
Student-Placement-Prediction/
│
├── app/                            # Core application package
│   ├── config/
│   │   └── schema.yaml             # Column schema and type definitions
│   └── src/
│       ├── components/             # Modular pipeline components
│       │   ├── data_ingestion.py       # Load, split, and save raw data
│       │   ├── data_validation.py      # Schema and column validation
│       │   ├── data_transformation.py  # Feature selection / column removal
│       │   ├── model_building.py       # Train and serialise the model
│       │   └── model_evaluation.py     # Evaluate and save metrics
│       ├── constants/
│       │   └── __init__.py         # All project-wide constants
│       ├── pipelines/
│       │   ├── training_pipeline.py    # Orchestrates the 5-step training flow
│       │   └── prediction_pipeline.py  # Converts form input → DataFrame → prediction
│       └── utils/
│           ├── config_reader.py    # YAML file reader utility
│           ├── exception.py        # Custom exception class
│           └── logger.py           # Structured logging setup
│
├── artifact/                       # Auto-generated pipeline outputs
│   ├── data_ingestion/
│   │   ├── train.csv               # 70% training split (~3,010 rows)
│   │   └── test.csv                # 30% test split (~1,290 rows)
│   ├── data_transformation/
│   │   ├── train_processed.csv     # Transformed training data
│   │   └── test_processed.csv      # Transformed test data
│   ├── data_validation/
│   │   └── data_validation_report.json
│   └── model_trainer/
│       └── model.pkl               # Serialised Logistic Regression model
│
├── frontend/                       # Flask web application UI
│   ├── static/
│   │   └── style.css               # Custom stylesheet
│   └── templates/
│       └── index.html              # Jinja2 prediction form template
│
├── notebooks/
│   └── Student Placement Prediction.ipynb  # EDA and model benchmarking
│
├── reports/
│   ├── figures/                    # Visualisation outputs (EDA screenshots, UI)
│   └── metrics/
│       └── metrics.json            # Final model evaluation metrics
│
├── logs/
│   └── log_info.log                # Pipeline execution logs
│
├── app.py                          # Flask entry point
├── demo.py                         # Training pipeline runner
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project packaging metadata
├── setup.sh                        # Package setup script
└── LICENSE                         # MIT License
```

---

## 🔄 Workflow

```
Raw Dataset (GitHub CSV)
        ↓
[ Step 1 ] Data Ingestion
   • Load CSV from remote URL
   • 70/30 train-test split (random_state=42)
   • Save train.csv and test.csv to artifact/
        ↓
[ Step 2 ] Data Validation
   • Validate all expected columns against schema.yaml
   • Verify target column (placement_status) presence
   • Export validation_report.json
        ↓
[ Step 3 ] Data Transformation
   • Drop irrelevant column: package_range
   • Save processed train/test CSVs
        ↓
[ Step 4 ] Model Building
   • Load processed training data
   • Train Logistic Regression (max_iter=2000, random_state=42)
   • Serialise model to model.pkl
        ↓
[ Step 5 ] Model Evaluation
   • Load test data and model.pkl
   • Compute Accuracy, Precision, Recall, F1
   • Save metrics to reports/metrics/metrics.json
        ↓
[ Prediction ] Flask Web App
   • User fills the 9-field form
   • Input → PredictionPipeline → DataFrame
   • Model predicts: Placed / Not Placed
   • Result rendered on index.html
```

---

## 📊 Dataset

| Property | Details |
|----------|---------|
| **Source** | [GitHub-hosted CSV](https://raw.githubusercontent.com/Rohitranelab/dataset/refs/heads/main/student_placement.csv) |
| **Total samples** | ~4,300 rows (split 70/30: ~3,010 train / ~1,290 test) |
| **Target variable** | `placement_status` — binary (1 = Placed, 0 = Not Placed) |
| **Missing values** | None detected (validation report: all columns present) |
| **Dropped column** | `package_range` (categorical, salary bracket — excluded from model input) |

**Input Features:**

| Feature | Type | Description |
|---------|------|-------------|
| `cgpa` | Float | Cumulative Grade Point Average (0–10 scale) |
| `projects` | Int | Number of projects completed |
| `communication_skills` | Float | Communication skill score (0–10) |
| `internship` | Int | Internship experience (1 = Yes, 0 = No) |
| `programming_skills` | Float | Programming skill score (0–10) |
| `technical_skills` | Float | Technical skill score (0–10) |
| `certifications` | Int | Number of certifications obtained |
| `aptitude` | Float | Aptitude test score (0–100 scale) |
| `interview_score` | Float | Interview performance score (0–100 scale) |

---

## 📈 Exploratory Data Analysis

The research notebook (`notebooks/Student Placement Prediction.ipynb`) covers the following key analyses:

**Univariate Analysis**
- CGPA distribution — histogram with KDE overlay
- Projects and certifications count distributions
- Internship participation — binary countplot
- Placement status class balance check
- Package range distribution (salary bracket breakdown)

**Multivariate Analysis**
- Correlation heatmap across all 9 numerical features using Seaborn

**Key Insights:**
- CGPA, interview score, aptitude, and technical skills show strong positive correlation with placement status
- Internship experience is a significant binary predictor
- The dataset exhibits a moderate class imbalance favouring placed students

> All EDA visualisations are saved under `reports/figures/`.

---

## 🔧 Data Preprocessing

| Step | Detail |
|------|--------|
| **Missing value handling** | No missing values detected in the dataset |
| **Encoding** | No encoding required — all features are already numeric |
| **Scaling** | StandardScaler applied in the research notebook for benchmarking; production model uses raw features |
| **Feature selection** | `package_range` (post-placement salary bracket) dropped — data leakage risk |
| **Outlier treatment** | Not explicitly applied; the dataset is pre-cleaned |
| **Train-test split** | 70% train / 30% test, `random_state=42` for reproducibility |

---

## 🤖 Models Used

All models below were benchmarked in the research notebook. The production pipeline uses Logistic Regression as the final deployed model.

| Model | Purpose | Library |
|-------|---------|---------|
| **Logistic Regression** | ✅ Final production model | Scikit-Learn |
| Decision Tree | Benchmarking — interpretable baseline | Scikit-Learn |
| Random Forest | Benchmarking — ensemble (100 estimators) | Scikit-Learn |
| Extra Trees | Benchmarking — randomised ensemble (100 estimators) | Scikit-Learn |
| AdaBoost | Benchmarking — boosting baseline | Scikit-Learn |
| Gradient Boosting | Benchmarking — staged boosting | Scikit-Learn |
| K-Nearest Neighbours | Benchmarking — instance-based (k=10) | Scikit-Learn |
| Support Vector Classifier | Benchmarking — kernel-based | Scikit-Learn |
| XGBoost | Benchmarking — optimised gradient boosting | XGBoost |

> Logistic Regression was selected for production due to its strong metrics, interpretability, fast inference, and minimal dependency footprint.

---

## 📉 Model Performance

Metrics evaluated on the **30% held-out test set** using the production Logistic Regression model:

| Metric | Score |
|--------|-------|
| **Accuracy** | **91.16%** |
| **Precision** | **91.73%** |
| **Recall** | **94.44%** |
| **F1-Score** | **93.07%** |

> Source: `reports/metrics/metrics.json` — generated automatically at the end of each training pipeline run.

> ROC-AUC, RMSE, MAE, and R² are not part of the current evaluation pipeline (binary classification task; regression metrics not applicable).

---

## ⚙️ Installation

**Prerequisites:** Python 3.11+, Git

```bash
# 1. Clone the repository
git clone https://github.com/Rohitranelab/Student-Placement-Prediction.git
cd Student-Placement-Prediction

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install the project package
pip install -e .
```

**`requirements.txt`**

```text
pandas
scikit-learn
xgboost
flask
```

---

## 🚀 Usage

### Step 1 — Run the Training Pipeline

This step downloads the dataset, validates it, transforms it, trains the model, and saves the evaluation metrics.

```bash
python demo.py
```

Expected output (via `logs/log_info.log`):

```
TRAINING AND PREDICTION PIPELINE STARTED
STEP 1: Data Ingestion completed successfully
STEP 2: Data Validation completed successfully
STEP 3: Data Transformation completed successfully
STEP 4: Model Building completed successfully
STEP 5: Model Evaluation completed successfully
TRAINING AND PREDICTION PIPELINE COMPLETED SUCCESSFULLY
```

### Step 2 — Launch the Web Application

```bash
python app.py
```

Then open your browser and navigate to:

```
http://localhost:5000
```

Fill in the 9 student feature fields and click **Predict Placement** to get an instant result.

---

## 🧪 Example Predictions

**Sample Input — Likely to be Placed:**

| Feature | Value |
|---------|-------|
| CGPA | 8.5 |
| Projects | 4 |
| Communication Skills | 8.0 |
| Internship | Yes (1) |
| Programming Skills | 7.5 |
| Technical Skills | 8.0 |
| Certifications | 3 |
| Aptitude | 78.0 |
| Interview Score | 82.0 |

**Prediction Output:**

```
Student is predicted to be: Placed ✅
```

---

**Sample Input — Likely Not Placed:**

| Feature | Value |
|---------|-------|
| CGPA | 5.2 |
| Projects | 0 |
| Communication Skills | 4.5 |
| Internship | No (0) |
| Programming Skills | 3.0 |
| Technical Skills | 3.5 |
| Certifications | 0 |
| Aptitude | 45.0 |
| Interview Score | 40.0 |

**Prediction Output:**

```
Student is predicted to be: Not Placed ❌
```

---

## 🖼 Visualizations

> The following plots are generated in the research notebook and saved to `reports/figures/`.

| Plot | Description |
|------|-------------|
| `cgpa_distribution.png` | CGPA histogram with KDE — shows the spread of academic performance |
| `projects_countplot.png` | Number of projects per student |
| `internship_countplot.png` | Internship experience distribution |
| `certifications_countplot.png` | Certifications obtained per student |
| `placement_status_countplot.png` | Class balance of the target variable |
| `package_range_distribution.png` | Salary bracket distribution for placed students |
| `correlation_heatmap.png` | Correlation matrix across all 9 numerical features |
| `ui_form.png` | Web application input form screenshot |
| `result_placed.png` | Web application — "Placed" result screenshot |
| `result_not_placed.png` | Web application — "Not Placed" result screenshot |

---

## 🔧 Configuration

All project-level constants are centralised in `app/src/constants/__init__.py`:

| Constant | Default | Description |
|----------|---------|-------------|
| `DATA_PATH` | GitHub raw CSV URL | Source dataset URL |
| `TARGET_COLUMN` | `placement_status` | Binary classification target |
| `COLUMN_NAME` | `["package_range"]` | Columns dropped during transformation |
| `ARTIFACT_DIR` | `artifact` | Root directory for pipeline outputs |
| `DATA_INGESTION_TRAIN_AND_TEST_SPLIT_RATIO` | `0.3` | Test set proportion |
| `DATA_INGESTION_RANDOM_STATE` | `42` | Train/test split seed |
| `MODEL_TRAINER_MAX_ITER` | `2000` | Logistic Regression max iterations |
| `MODEL_TRAINER_RANDOM_STATE` | `42` | Model training seed |
| `SCHEMA_FILE_PATH` | `app/config/schema.yaml` | Column schema definition path |

Column schema is managed separately in `app/config/schema.yaml` for easy updates without touching Python code.

---

## 🗺 Future Improvements

- [ ] **Hyperparameter tuning** — GridSearchCV / RandomizedSearchCV for Logistic Regression
- [ ] **Model selection automation** — auto-pick the best model from the benchmark results
- [ ] **Explainability** — SHAP or LIME integration to explain individual predictions
- [ ] **Docker containerisation** — Dockerfile + docker-compose for one-command deployment
- [ ] **Cloud deployment** — Render, Heroku, or AWS EC2 for a publicly accessible live demo
- [ ] **CI/CD pipeline** — GitHub Actions for automated testing and deployment
- [ ] **Feature engineering** — interaction terms, polynomial features, or domain-derived aggregates
- [ ] **Model monitoring** — track prediction drift over time with Evidently AI or similar
- [ ] **REST API** — expose `/predict` endpoint as a JSON API for third-party integrations
- [ ] **Unit tests** — pytest coverage for all pipeline components and utility functions
- [ ] **Streamlit dashboard** — richer UI with charts, SHAP plots, and batch prediction upload

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and add tests where applicable
4. Commit with a descriptive message: `git commit -m "feat: add SHAP explainability support"`
5. Push to your fork: `git push origin feature/your-feature-name`
6. Open a Pull Request against the `main` branch

Please ensure your code follows the existing structure — new pipeline steps belong in `app/src/components/`, constants in `app/src/constants/__init__.py`, and all paths managed via the `ARTIFACT_DIR` constant.

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License — Copyright (c) 2026 Rohit Rane
```

See the full [LICENSE](LICENSE) file for details.

---

## 👤 Author

<div align="center">

**Rohit Rane**

[![GitHub](https://img.shields.io/badge/GitHub-Rohitranelab-181717?style=for-the-badge&logo=github)](https://github.com/Rohitranelab)
[![Email](https://img.shields.io/badge/Email-ranerohit996@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ranerohit996@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/your-linkedin-handle)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-4CAF50?style=for-the-badge)](https://your-portfolio-url.com)

</div>

---

## 🙏 Acknowledgements

- **Dataset** — Hosted on [Rohitranelab/dataset](https://github.com/Rohitranelab/dataset) (GitHub)
- **Scikit-Learn** — Core ML framework for model training, evaluation, and data splitting
- **XGBoost** — Gradient boosting benchmarking in the research phase
- **Flask** — Lightweight and elegant web application framework
- **Seaborn / Matplotlib** — Visualisation libraries used in the EDA notebook
- **MLOps community** — Architectural patterns and component-based pipeline design inspiration

---

## 🌟 Why This Project Stands Out

> *Designed to impress — built with engineering discipline.*

✔ **End-to-end ML pipeline** — from raw data ingestion to a live web prediction interface  
✔ **MLOps-ready architecture** — modular components, pipelines, constants, and utilities are cleanly separated  
✔ **Production-grade logging** — every pipeline step produces structured, timestamped logs  
✔ **Schema-driven validation** — data quality checked automatically against `schema.yaml` before training  
✔ **Configurable constants** — no magic strings; all parameters centralised and documented  
✔ **Custom exception handling** — rich error messages with source file and line number context  
✔ **Multi-model research notebook** — 9 algorithms benchmarked before selecting the production model  
✔ **Reproducible experiments** — fixed random seeds throughout ensure identical results on re-runs  
✔ **Flask web deployment** — real users can interact with the model through a clean UI  
✔ **Professional documentation** — this README serves as a complete project reference

---

<div align="center">

Made with ❤️ by [Rohit Rane](https://github.com/Rohitranelab)

⭐ If you found this project useful, please consider giving it a star!

</div>