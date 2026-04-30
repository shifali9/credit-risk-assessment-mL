import streamlit as st
import pickle
import numpy as np

# Load model (make sure model.pkl is in same folder)
model = pickle.load(open("C:/Users/Roshni/OneDrive/MSC/2ND SEM/ML/model.pkl", "rb"))
# Title
st.title("💳 Credit Risk Prediction System")

st.write("Enter applicant details:")

# Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)

sex = st.selectbox("Sex", ["Male", "Female"])
sex = 0 if sex == "Male" else 1

job = st.selectbox("Job", [
    "Unemployed (0)",
    "Unskilled (1)",
    "Skilled (2)",
    "Highly Skilled (3)"
])
job = ["Unemployed (0)", "Unskilled (1)", "Skilled (2)", "Highly Skilled (3)"].index(job)

housing = st.selectbox("Housing", ["Own (0)", "Rent (1)", "Free (2)"])
housing = ["Own (0)", "Rent (1)", "Free (2)"].index(housing)

saving = st.selectbox("Saving Account", [
    "Little (0)", "Moderate (1)", "Rich (2)", "Quite Rich (3)", "Unknown (4)"
])
saving = ["Little (0)", "Moderate (1)", "Rich (2)", "Quite Rich (3)", "Unknown (4)"].index(saving)

checking = st.selectbox("Checking Account", [
    "Little (0)", "Moderate (1)", "Rich (2)", "Unknown (3)"
])
checking = ["Little (0)", "Moderate (1)", "Rich (2)", "Unknown (3)"].index(checking)

duration = st.number_input("Duration (months)", min_value=1, max_value=72, value=12)

purpose = st.selectbox("Purpose", [
    "Car (0)", "Furniture (1)", "Radio (2)",
    "Education (3)", "Business (4)", "Others (5)"
])
purpose = ["Car (0)", "Furniture (1)", "Radio (2)",
           "Education (3)", "Business (4)", "Others (5)"].index(purpose)

# Prediction button
if st.button("Predict Risk"):
    input_data = np.array([[age, sex, job, housing, saving, checking, duration, purpose]])

    prob = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result:")

    if prob < 0.4:
        st.success(" Low Risk")
    elif prob < 0.8:
        st.warning("Medium Risk")
    else:
        st.error("High Risk")