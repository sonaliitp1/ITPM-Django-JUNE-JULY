from sklearn.impute import SimpleImputer
import numpy as np
data = np.array([
    [4,5,np.nan],
    [10,np.nan,23],
    [np.nan,20,12]
])

imputerobj = SimpleImputer(strategy="mean")

newarray = imputerobj.fit_transform(data)
print(data)
print(newarray)