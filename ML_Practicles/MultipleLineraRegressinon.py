from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'Experience': [1, 2, 3, 4, 5],
    'Education': [1, 2, 2, 3, 3],
    'Salary': [15000, 20000, 25000, 30000, 35000]
})

# Features and target
X = data[['Experience', 'Education']]
y = data['Salary']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)


exp = float(input("Enter Experience (years): "))
edu = float(input("Enter Education level: "))

user_data = pd.DataFrame([[exp, edu]], columns=['Experience', 'Education'])

# Prediction
prediction = model.predict(user_data)

print("Predicted Salary:", prediction[0]) 