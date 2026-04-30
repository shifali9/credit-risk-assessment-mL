# Intelligent Credit Risk Assessment System

This project predicts whether a person is a credit risk for loan approval using Machine Learning.

## Objective
To classify customers as low or high credit risk based on their details.

## Dataset
German Credit Dataset  
Link: https://www.kaggle.com/datasets/uciml/german-credit

## Project Structure

- **Credit_Risk_model.ipynb** — Data preprocessing, training & evaluation  
- **app.py** — Streamlit web application  
- **risk_predictor.py** — Command-line interface (CLI) for prediction   
- **model.pkl** — Trained model  
- **german_credit_data.csv** — Dataset  
- **README.md** — Documentation  

## How to Run

Follow the steps below to run the Streamlit web application.

### Requirements
- Python 3.x
- Streamlit

### Steps

1. Open Command Prompt

2. Navigate to the project folder:
   cd credit-risk-assessment-ML

3. Install dependencies:
   pip install streamlit

4. Run the application:
   python -m streamlit run app.py

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
- Model performance evaluated using ROC-AUC score and accuracy

## Conclusion
Random Forest outperformed Logistic Regression, indicating that ensemble methods capture complex patterns better in this dataset.
