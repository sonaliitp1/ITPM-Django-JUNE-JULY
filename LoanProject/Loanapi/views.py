from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import joblib
import os

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'loan_model.pkl')
model = joblib.load(model_path)


@api_view(['GET'])
def home(request):
    return Response({
        "message": "Loan Prediction Django API Running"
    })

@api_view(['POST'])
def predict(request):
    try:
        data = request.data

        input_data = pd.DataFrame({
            'Gender': [data['Gender']],
            'Married': [data['Married']],
            'Dependents': [data['Dependents']],
            'Education': [data['Education']],
            'Self_Employed': [data['Self_Employed']],
            'ApplicantIncome': [data['ApplicantIncome']],
            'CoapplicantIncome': [data['CoapplicantIncome']],
            'LoanAmount': [data['LoanAmount']],
            'Loan_Amount_Term': [data['Loan_Amount_Term']],
            'Credit_History': [data['Credit_History']],
             'Property_Area': [data['Property_Area']]
        })

        prediction = model.predict(input_data)

        result = "Approved" if prediction[0] == 1 else "Rejected"

        return Response({
            "Loan Status": result
        })

    except Exception as e:
        return Response({
            "error": str(e)
        })