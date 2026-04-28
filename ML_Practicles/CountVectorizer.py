from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love machine learning",     # 4*7 [0 0 0 0 0 1 1 1 ]
    "Machine learning is fun",     # [0 0 0 1 1 1 0 1]
    "I love coding",
    "Coding is fun and exciting"
]

vector = CountVectorizer()

newarray = vector.fit_transform(documents)

feature_names = vector.get_feature_names_out()

print("Feature Names:-",feature_names)

print("Vocabulaory:-",vector.vocabulary_)

print("Text to Number Conversion :- ",newarray.toarray())
