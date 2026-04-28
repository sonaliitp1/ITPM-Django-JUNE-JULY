from sklearn.preprocessing import OneHotEncoder 
import pandas as pd

data = pd.DataFrame({
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']
})

oneobj = OneHotEncoder()

newarray = oneobj.fit_transform(data[['City']])

print(newarray.toarray())


   