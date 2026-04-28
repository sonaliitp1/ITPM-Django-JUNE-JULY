
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataset
X = [[2.0,3.0], [3.0, 4.0], [5.0, 6.0], [7.0, 8.0], [10.0, 10.0]]
y = ['A', 'A', 'B', 'B', 'A']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

# Model
model = KNeighborsClassifier(n_neighbors=2)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

print("Prediction :-",y_pred[0])
# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
