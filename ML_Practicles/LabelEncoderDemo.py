import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.DataFrame({
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']
})

le = LabelEncoder()

data['City_Label'] = le.fit_transform(data['City'])

print(data)
