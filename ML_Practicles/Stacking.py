from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

X = np.array([[2, 40],
              [3, 45],
              [8, 85],
              [9, 90]])

estimators = [
    ('dt', DecisionTreeClassifier()),
    ('knn', KNeighborsClassifier())
]

model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)

'''
estimators
List of base models (Decision Tree + KNN)
final_estimator=LogisticRegression()
This is the meta model (level-1 model)
It learns how to combine predictions of base models
model.fit(X_train, y_train)

'''

print("Accuracy:", model.score(X_test, y_test))