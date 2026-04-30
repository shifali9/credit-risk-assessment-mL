# Intelligent Credit Risk Assessment System

This project predicts whether a person is risky for giving a loan using Machine Learning.

## Objective
To classify customers as low or high credit risk based on their details.

## Dataset
German Credit Dataset  
Link: https://www.kaggle.com/datasets/uciml/german-credit

## Project Structure

credit-risk-assessment-ML/
│
├── Credit_Risk_model.ipynb   # Data preprocessing, training & evaluation
├── app.py                    # Web application interface
├── risk_predictor.py         # CLI-based prediction tool
├── model.pkl                 # Saved trained model
├── german_credit_data.csv    # Input dataset
├── README.md                 # Documentation

## How to Run

### Requirements
- Python 3.x
- Streamlit

### Steps

1. Clone the repository:
   git clone https://github.com/shifali9/credit-risk-assessment-ML.git

2. Navigate to the project folder:
   cd credit-risk-assessment-ML

3. Install dependencies:
   pip install pandas numpy scikit-learn streamlit

4. Run the application:
   streamlit run app.py

5. Open the URL shown in the terminal (usually http://localhost:8501/)

## Features Used
- Age
- Sex
- Job
- Housing
- Saving accounts
- Checking account
- Credit amount
- Duration
- Purpose

## Models Used
- Logistic Regression
- Random Forest

## Evaluation
- ROC-AUC Score used for performance
- Model achieved very high accuracy

## Conclusion
Random Forest outperformed Logistic Regression, indicating that ensemble methods capture complex patterns better in this dataset.
