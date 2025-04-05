import streamlit as st
import joblib
import numpy as np
performance_model=joblib.load('performance_mode.pk1')
attrition_model=joblib.load('attrition_model.pk1')
st.title("Employee performance & attrition Predictor")
st.sidebar.header("Employee Info")
age=st.sidebar.slider("Age",18,60,30)
education=st.sidebar.slider("Education level",[1,2,3,4,5])
job_level=st.sidebar.slider("job level",1,5,2)
monthly_income=st.sidebar.numer_input("monthly Income",1000,20000,5000)
years_at_company=st.sidebar("Years at company",0,40,5)
overtime=st.sidebar.selectbox("Overtime",["Yes","No"])
overtime_num=1 if overtime =="Yes" else 0
features=np.array([[age,education,job_level,monthly_income,years_at_company,overtime_num]])
if st.button("Predict"):
    performance_pred=performance_model.predict(features)[0]
    attrition_pred=attrition_model.predict(features)[0]
    attrition_proba=attrition_model.predict_proba(features)[0][1]
    st.subheadr("Results")
    st.write(f" predicted performance score: {round(performance_pred,2)}")
    st.write(f" Attrition Risk:{'Yes' if attrition_pred ==1 else 'No'} ({round(attrition_proba*100,1)}%)")
    