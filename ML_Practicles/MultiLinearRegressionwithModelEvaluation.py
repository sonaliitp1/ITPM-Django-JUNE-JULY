# ==============================
# 1. Import Libraries
# ==============================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib

# ==============================
# 2. Create Dataset (Sample Data)
# ==============================
data = pd.DataFrame({
    'Area': [1000, 1500, 2000, 2500, 3000, 3500],
    'Bedrooms': [2, 3, 3, None, 4, 5],
    'Bathrooms': [1, 2, 2, None, 3, 4],
    'Location': ['Pune', 'Mumbai', 'Pune', 'Mumbai', 'Pune', 'Mumbai'],
    'Price': [50, 75, 100, 130, 150, 180]  # in lakhs
})

print("Dataset:\n", data)

#Use fillna() (Before Encoding & Training)

data['Area'] = data['Area'].fillna(data['Area'].mean())
data['Bedrooms'] = data['Bedrooms'].fillna(data['Bedrooms'].mean())
data['Bathrooms'] = data['Bathrooms'].fillna(data['Bathrooms'].mean())
data['Price'] = data['Price'].fillna(data['Price'].mean())


# Fill with Median (Better for Outliers)

data['Area'] = data['Area'].fillna(data['Area'].median())

# Fill Categorical Values
data['Location'] = data['Location'].fillna(data['Location'].mode()[0])  --

#Fill All at Once
# Numerical columns
num_cols = ['Area', 'Bedrooms', 'Bathrooms', 'Price']
data[num_cols] = data[num_cols].fillna(data[num_cols].mean())

# 3. Preprocessing

# Convert categorical data (Location) into numerical
data = pd.get_dummies(data, columns=['Location'], drop_first=True)
   

'''
pd.get_dummies() is used to convert categorical variables into numerical using one-hot encoding.
drop_first=True is used to remove one dummy variable to avoid multicollinearity.
'''

print("\nAfter Encoding:\n", data)


# 4. Define Features & Target

X = data.drop('Price', axis=1)
y = data['Price']


# 5. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# 6. Feature Scaling (Optional)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  #fit() learns the statistics from the data:Mean (average)
                                          #Standard deviation(Model should learn from training data only)

X_test = scaler.transform(X_test)  #It applies the formula using the learned mean & std
                                    #It converts data into scaled values(Test data must remain unseen (new data))


# 7. Train Model

model = LinearRegression()
model.fit(X_train, y_train)


# 8. Model Parameters

print("\nIntercept:", model.intercept_) # It is the base value of Price when all input features = 0
print("Coefficients:", model.coef_) # How much the price changes when each feature increases by 1 unit

# Price = 10 lakh
#       + (0.05 × Area) 
#       + (10 × Bedrooms) 
#       + (5 × Bathrooms) 
#       + (20 × Location_Mumbai) # in intercept Without scaling	Real base value
                                 # With scaling	Approx average of target

# 9. Predictions
y_pred = model.predict(X_test)

print("\nPredicted Values:", y_pred)   -- 20
print("Actual Values:", list(y_test))  --- 50


# 10. Model Evaluation

# print("\nR2 Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))


# 11. Predict New Data

# Format: [Area, Bedrooms, Bathrooms, Location_Mumbai]
# (Location_Mumbai = 1 if Mumbai, 0 if Pune)

new_house = [[2200, 3, 2, 0]]  # Pune house

new_house_scaled = scaler.transform(new_house)
predicted_price = model.predict(new_house_scaled)

print("\nPredicted Price for new house:", predicted_price[0], "lakhs")



''''
1. Intercept (model.intercept_)

It is the starting value of y when all inputs = 0

Example
Intercept: 10

Meaning:

If Area = 0, Bedrooms = 0, Bathrooms = 0
Price = 10 (base price)

2. Coefficients (model.coef_)

These show how much each feature affects the output

Example Output -

Coefficients: [0.05, 10, 5]

Assume:

Area → 0.05
Bedrooms → 10
Bathrooms → 5

Area = 0.05
If area increases by 1 unit → price increases by 0.05
Bedrooms = 10
Adding 1 bedroom → price increases by 10
Bathrooms = 5
Adding 1 bathroom → price increases by 5
'''