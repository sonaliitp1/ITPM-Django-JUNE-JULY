from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Dataset
df = pd.DataFrame({
    "Hours": [1,2,3,4,5],
    "Pass": [0,0,1,1,1]
})

X = df[["Hours"]]
y = df[["Pass"]]

# Model
model = RandomForestClassifier(n_estimators=5, random_state=42)   # n_estimators →                                                                                      number                               of trees
								    
								                                #random_state → reproducibility(Getting the same result every time you run the same code 								    with the same data.)
model.fit(X, y)

# Prediction
prediction = model.predict([[2]])
print("Prediction:", prediction)