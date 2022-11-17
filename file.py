
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree, preprocessing
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


url = "https://philchodrow.github.io/PIC16A/datasets/palmer_penguins.csv"
penguins = pd.read_csv(url)

penguins = penguins[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)', 'Species']]
penguins = penguins.dropna()
np.random.seed(3354354524)
y = penguins["Species"]
X = penguins[['Island', 'Body Mass (g)', 'Delta 15 N (o/oo)', 'Delta 13 C (o/oo)']].copy()

le = preprocessing.LabelEncoder()
X['Island'] = le.fit_transform(X['Island'])
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

T = tree.DecisionTreeClassifier(max_depth=3) 
T.fit(X_train, y_train)
print(T.score(X_train, y_train))
print(T.score(X_test, y_test))


