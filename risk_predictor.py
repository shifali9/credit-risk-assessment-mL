import pandas as pd
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("c:/Users/Roshni/OneDrive/MSC/2ND SEM/ML/model.pkl", "rb"))
print("Enter Applicant Details:")

age = int(input("Age: "))

sex = int(input("Sex (0 = male, 1 = female): "))

job = int(input("Job (0 = unemployed, 1 = unskilled, 2 = skilled, 3 = highly skilled): "))

housing = int(input("Housing (0 = own, 1 = rent, 2 = free): "))

saving = int(input("Saving accounts (0 = little, 1 = moderate, 2 = rich, 3 = unknown): "))

checking = int(input("Checking account (0 = little, 1 = moderate, 2 = rich, 3 = unknown): "))

duration = int(input("Duration (months): "))

purpose = int(input("Purpose (0 = car, 1 = furniture, 2 = radio, 3 = education, 4 = business, 5 = others): "))

# Create input array
data = np.array([[age, sex, job, housing, saving, checking, duration, purpose]])

# Prediction
prob = model.predict_proba(data)[0][1]

print("Risk Probability:", prob)

if prob < 0.4:
    print("Low Risk")
elif prob < 0.8:
    print("Medium Risk")
else:
    print("High Risk")

# Example prediction (for GitHub display)
import numpy as np

input_data = np.array([[23, 1, 2, 2, 1, 1, 12, 0]])
prob = model.predict_proba(input_data)[0][1]
print("Prediction Result:", prob)