from sklearn.preprocessing import StandardScaler
import pandas as pd 

data =pd.DataFrame({
    "salary":[20000, 50000, 80000, 40000, 70000]
})

stdobj = StandardScaler()

newarray = stdobj.fit_transform(data)

print(newarray)

