import numpy as np
from sklearn.cluster import KMeans

# Dataset
X = np.array([[2, 40],
              [3, 45],
              [8, 85],
              [9, 90]])

# Create model
model = KMeans(n_clusters=2, random_state=42) #You want 2 groups (clusters) ensures same result every time

# Train model
model.fit(X)

# Cluster labels for existing data
print("Cluster Labels:", model.labels_) # First two students → Cluster 0
                                        # Last two students → Cluster 1

# Centroids
print("Centroids:\n", model.cluster_centers_) #These are the center points of clusters
                                              # Cluster 0	(2.5, 42.5)
                                              # Cluster 1	(8.5, 87.5)
                                              # Now we check which cluster this new point belongs to.
                                              # Distance from centroids:Clearly closer to (2.5, 42.5)

# Prediction (NEW DATA)
new_student = [[4, 50]]

prediction = model.predict(new_student)

print("Predicted Cluster:", prediction)