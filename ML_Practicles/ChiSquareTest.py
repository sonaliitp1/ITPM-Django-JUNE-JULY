from sklearn.feature_selection import SelectKBest,chi2
from sklearn.preprocessing import LabelEncoder
import pandas as pd

data = pd.DataFrame({
    'Age': [25, 30, 45, 35, 50],
    'Salary': [20000, 30000, 50000, 40000, 60000],
    'Experience': [1, 3, 10, 5, 12],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi'],
    'Purchased': [0, 1, 1, 0, 1]
})

obj = SelectKBest(score_func=chi2,k=2)

le = LabelEncoder()

data['City'] = le.fit_transform(data['City'])

X = data[['Age','Salary','Experience','City']]

Y = data['Purchased']

newarray = obj.fit_transform(X,Y)

print(newarray)

