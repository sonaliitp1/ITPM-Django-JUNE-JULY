from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np
X = np.array([[2, 40],
              [3, 45],
              [8, 85],
              [9, 90]])

model = AdaBoostClassifier(
    base_estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50
)

'''

base_estimator=DecisionTreeClassifier(max_depth=1)-

You are using a decision stump (a tree with only 1 split).
This is a weak learner (simple model with low accuracy).
n_estimators=50
AdaBoost will create 50 weak learners.
These learners are trained sequentially.

How AdaBoost works internally 


1. Initially, all training data points have equal weight.
2. Train first weak model.
3. Check which points are misclassified.
4. Increase weights of misclassified points.
5. Train next model focusing more on difficult points.
6. Repeat this process for 50 models.

 Final prediction = weighted combination of all models

'''

model.fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))