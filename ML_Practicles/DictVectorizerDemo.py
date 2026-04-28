from sklearn.feature_extraction import DictVectorizer

data = [
    {'age': 25, 'city': 'Pune'},
    {'age': 30, 'city': 'Mumbai'},
    {'age':45,  'city':'Pune'},
    {'age':67,'city':'Amahadabad'}
]

dictobj = DictVectorizer(sparse=False)

newarray = dictobj.fit_transform(data)

features_names = dictobj.get_feature_names_out()

print(features_names)

print(newarray)