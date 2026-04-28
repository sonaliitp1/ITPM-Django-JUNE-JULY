# Loan Approval Prediction System
# Complete Machine Learning Project Code

# Step 1: Import Libraries
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 2: Load Dataset
# Make sure your file name is: loan_data.csv

df = pd.read_csv("loan_data.csv")

# Display first 5 rows
print("First 5 Rows of Dataset:")
print(df.head())

# Display dataset information
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Step 3: Fill Missing Values

# For numerical columns
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mean())

# For categorical columns
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])

# Step 4: Drop unnecessary column
df = df.drop('Loan_ID', axis=1)

# feature scaling

# Step 5: Convert Categorical Data into Numerical Data
label_encoder = LabelEncoder()

categorical_columns = [
    'Gender',
    'Married',
    'Dependents',
    'Education',
    'Self_Employed',
    'Property_Area',
    'Loan_Status'
]

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# Step 6: Define Features and Target

X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

# Step 7: Split Dataset into Training and Testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Step 8: Create Model

model = DecisionTreeClassifier(random_state=42)

# Step 9: Train Model

model.fit(X_train, y_train)

# Step 10: Prediction

y_pred = model.predict(X_test)

# Step 11: Evaluation

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 12: Predict New Data

sample_data = pd.DataFrame({
    'Gender': [1],
    'Married': [1],
    'Dependents': [0],
    'Education': [0],
    'Self_Employed': [0],
    'ApplicantIncome': [5000],
    'CoapplicantIncome': [2000],
    'LoanAmount': [150],
    'Loan_Amount_Term': [360],
    'Credit_History': [1],
    'Property_Area': [2]
})

prediction = model.predict(sample_data)

print("\nLoan Prediction for New Applicant:")

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")

# step 13
    # save model
joblib.dump(model, "loan_model.pkl")
print("Model saved successfully")

# 1. create new Django project - django-admin startproject  LoanProject

# 2. create new app -  django-admin startapp loanapi 

# 3. pip install djangorestframework,joblib,

