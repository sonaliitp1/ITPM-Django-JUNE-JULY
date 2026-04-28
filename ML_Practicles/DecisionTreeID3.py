import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import matplotlib.pyplot as plt


data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# 2. Encode Categorical Datale_outlook = LabelEncoder()   #Label Encoding Since machine learning models need numbers:

le_temp = LabelEncoder()
le_play = LabelEncoder()
le_outlook = LabelEncoder()

df['Outlook'] = le_outlook.fit_transform(df['Outlook'])
df['Temperature'] = le_temp.fit_transform(df['Temperature'])
df['Play'] = le_play.fit_transform(df['Play'])


# 3. Features & Target

X = df[['Outlook', 'Temperature']]
y = df['Play']


# 4. Train ID3 Model (Entropy)

model = DecisionTreeClassifier(criterion='entropy')  #This makes the model behave like ID3
						                              #Uses Information Gain
model.fit(X, y)

# 5. Predict Example

# Example: Outlook=Sunny, Temperature=Hot
sample = [[le_outlook.transform(['Sunny'])[0],     # Converts categorical value → numerical value
           le_temp.transform(['Hot'])[0]]]         # [0] -transform() returns a list/array
							                       #  We need only the value inside it [2] → 2

                                                   # why [[]] - Model expects 2D array

prediction = model.predict(sample)

print("Prediction:", le_play.inverse_transform(prediction))  #Convert Back to Original Label Model gives numeric output: 0 we want "No"					