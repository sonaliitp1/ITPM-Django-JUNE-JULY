from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

data={'Hours_study':[2,3,4,5,6,7,8,9,10],'Exam_score':[50,60,70,75,80,85,90,92,95]}
df = pd.DataFrame(data)

X = df[['Hours_study']]
Y = df[['Exam_score']]

X_train,X_test ,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)

linearmodel = LinearRegression()
linearmodel.fit(X_train,Y_train)

user_input=float(input("Enter the number of hours you study:")) 

predicted_score=linearmodel.predict([[user_input]])

#priting the output
print(f"Predicted Exam Score:{predicted_score.round(2)}")


