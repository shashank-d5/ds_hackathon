# HR Analytics: Employee Performance & Retention Prediction

This project focuses on predicting employee performance and retention using machine learning techniques. The goal is to help HR departments identify high-performing employees and those at risk of leaving the company.

##  Problem Statement

Human Resource (HR) analytics is a data-driven approach to managing people at work. In this project, we aim to:

- Predict employee performance
- Predict employee retention (whether an employee is likely to stay or leave)

##  Project Pipeline

1. **Data Collection**
2. **Data Cleaning & Preprocessing**
3. **Exploratory Data Analysis (EDA)**
4. **Feature Engineering**
5. **Model Training & Evaluation**
6. **Prediction & Insights**

##  Data Preprocessing

- Removed duplicates and null values
- Encoded categorical features using Label Encoding
- Removes irrevelant columns

##  Features Considered

- Age, Department, Education, Gender
- Business Travel, JobRole, Job Satisfaction
- SalarySlab, Overtime , PercentSalaryHike
- YearsAtCompany, TotalWorkingYears,etc.

##  Models Used

- Logistic Regression
- RandomForestRegression
- RandomForestClassifier

Model selection was based on accuracy, precision, recall, and F1-score.

##  Evaluation Metrics

- RMSE
- Accuracy
- Precision
- Recall
- F1 score

##  Streamlit Web Application

The project is deployed as a Streamlit web application to allow users to interactively:

- Predict employee performance score based on input data
- Predict the likelihood of employee attrition
- Use a simple, user-friendly form for entering details
- View model predictions in real-time

##  PowerBi Dashboard

We also created a Power BI dashboard to provide an interactive visualization of key HR insights:

Attrition rate by department, education, and gender

KPI and performance distribution

Correlation between training scores and retention

Trends and patterns in employee service length

The Power BI dashboard helps HR professionals understand workforce trends visually and make informed decisions.

##  Repository Structure

```
├── ds_hackathon.ipynb         # Main Jupyter notebook
├── README.md                  # Project overview
├── requirements.txt           # Python dependencies
|── powerbi_dashboard.pdf      # Dashboard created using PowerBi
|── requirements.txt           # Project requirements
|── st.py                      # Stremlit web application code
└── HR_Analytics.csv           # Dataset
```

##  Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/hr-analytics.git
   cd hr-analytics
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the notebook:
   ```bash
   jupyter notebook ds_hackathon.ipynb
   ```

##  Future Work

- Use SHAP/LIME for interpretability
- Incorporate time-series trends in predictions


