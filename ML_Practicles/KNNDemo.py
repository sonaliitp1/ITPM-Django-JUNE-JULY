from sklearn.impute import KNNImputer
import numpy as np

data =np.array([
    [2,4,np.nan],
    [5,1,6],
    [np.nan,5,7],
    [9,8,9]
])

knnobj = KNNImputer(n_neighbors=2)

newarr = knnobj.fit_transform(data)

print(data)
print(newarr)