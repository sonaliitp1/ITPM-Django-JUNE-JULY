import pandas as pd

data = pd.DataFrame({
    'Age': [25, 30, 45, 35, 50],
    'Salary': [20000, 30000, 50000, 40000, 60000],
    'Experience': [1, 3, 10, 5, 12],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi'],
    'Purchased': [0, 1, 1, 0, 1]
})

print(data.corr(numeric_only=True).round(2))
