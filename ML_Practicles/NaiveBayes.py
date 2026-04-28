import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


data = pd.DataFrame({
    'Hours_Study': [1, 2, 3, 4, 5, 6, 7, 8],
    'Attendance': [50, 60, 65, 70, 75, 80, 85, 90],
    'Pass': [0, 0, 0, 1, 1, 1, 1, 1]
})


# 3. Split Features & Target

X = data[['Hours_Study', 'Attendance']]
y = data['Pass']

# 4. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,   # 25% test data
    random_state=42
)

# 5. Train Model

model = GaussianNB()
model.fit(X_train, y_train)

# 6. Predictions
y_pred = model.predict(X_test)

# 7. Evaluation

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8. Test with New Data

new_data = [[5, 78]]  # 5 hours study, 78% attendance
prediction = model.predict(new_data)

print("\nPrediction for new student:", "Pass" if prediction[0] == 1 else "Fail")