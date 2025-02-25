import streamlit as st
import pickle
import pandas as pd

# Load Model
def load_pipeline():
    with open("cancer_pipeline.pkl", "rb") as f:
        return pickle.load(f)

# App UI
st.set_page_config(page_title="Cancer Prediction", layout="centered")
st.title("🩺 Cancer Prediction App")
st.write("Enter the patient details below to predict the likelihood of cancer.")

# Sidebar Inputs
st.sidebar.header("Patient Details")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=30)
tumor_size = st.sidebar.number_input("Tumor Size (mm)", min_value=0.0, max_value=200.0, value=10.0)
tumor_grade = st.sidebar.selectbox("Tumor Grade", ["Low", "Medium", "High"])
symptoms_severity = st.sidebar.selectbox("Symptoms Severity", ["Mild", "Moderate", "Severe"])
alcohol_consumption = st.sidebar.selectbox("Alcohol Consumption", ["Never", "Occasionally", "Frequently"])
exercise_frequency = st.sidebar.selectbox("Exercise Frequency", ["Never", "Rarely", "Often"])
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
smoking_history = st.sidebar.selectbox("Smoking History", ["Never", "Former Smoker", "Current Smoker"])
family_history = st.sidebar.selectbox("Family History of Cancer", ["No", "Yes"])

# Prepare input data
input_data = pd.DataFrame([[age, tumor_size, tumor_grade, symptoms_severity, 
                            alcohol_consumption, exercise_frequency, gender, 
                            smoking_history, family_history]],
                          columns=["Age", "Tumor_Size", "Tumor_Grade", "Symptoms_Severity", 
                                   "Alcohol_Consumption", "Exercise_Frequency", "Gender", 
                                   "Smoking_History", "Family_History"])

# Load model
model = load_pipeline()

# Predict button
if st.sidebar.button("Predict"):
    prediction = model.predict(input_data)
    result = "🛑 Cancer Detected" if prediction[0] == 1 else "✅ No Cancer"
    color = "red" if prediction[0] == 1 else "green"
    st.markdown(f"<h2 style='text-align: center; color: {color};'>{result}</h2>", unsafe_allow_html=True)
