
# 1. Import Libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



# 2. Create Dataset (500 Students)

np.random.seed(42)

data_size = 500

data = pd.DataFrame({
    'Study_Hours': np.random.randint(1, 10, data_size),
    'Attendance': np.random.randint(50, 100, data_size),
    'Previous_Score': np.random.randint(30, 100, data_size)
})



# 3. Create Target Variable (Pass/Fail Logic)

data['Pass'] = (
    (data['Study_Hours'] > 5).astype(int) +
    (data['Attendance'] > 75).astype(int) +
    (data['Previous_Score'] > 50).astype(int)
)

# If at least 2 conditions satisfied → Pass
data['Pass'] = (data['Pass'] > 1).astype(int)



# 4. Split Features & Target

X = data[['Study_Hours', 'Attendance', 'Previous_Score']]
y = data['Pass']



# 5. Train-Test Split
# ============================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)



# 6. Feature Scaling
# ============================================
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 7. Train Model
# ============================================
model = LogisticRegression()
model.fit(X_train, y_train)



# 8. Prediction
# ============================================
y_pred = model.predict(X_test)


# 9. Evaluation
# ============================================
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

print("\nClassification Report:\n", classification_report(y_test, y_pred))



# 10. Predict New Student
# ============================================
new_student = pd.DataFrame({
    'Study_Hours': [7],
    'Attendance': [80],
    'Previous_Score': [60]
})

new_student_scaled = scaler.transform(new_student)

prediction = model.predict(new_student_scaled)

print("\nPrediction (0=Fail, 1=Pass):", prediction[0])