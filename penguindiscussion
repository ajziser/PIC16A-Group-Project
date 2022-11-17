import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree, preprocessing
import numpy as np

url = "https://philchodrow.github.io/PIC16A/datasets/palmer_penguins.csv"
penguins = pd.read_csv(url)

penguins = penguins[["Species", "Flipper Length (mm)", "Body Mass (g)", "Sex"]]
penguins.head()

penguins = penguins.dropna()
penguins.head()

#penguins.drop(["Sex", "."])
penguins = penguins[penguins["Sex"] != "."]
penguins.shape

np.random.seed(3354354524)

from sklearn import preprocessing # scikit-learn is actually sklearn
le = preprocessing.LabelEncoder() # makes an instance of labelencoder
penguins['Sex'] = le.fit_transform(penguins["Sex"]) # turn 'female' to 0 and 'male' to 1

y = penguins["Species"]
X = penguins.drop(["Species"], axis = 1)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8)


print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


from sklearn import tree
T = tree.DecisionTreeClassifier(max_depth=20)
T.fit(X_train, y_train)

print(T.score(X_test, y_test))
print(T.score(X_train, y_train))
#print(str(testScore = T.score(X_test, y_test)))



fig, ax = plt.subplots(1, 1, figsize=(10,10))
p = tree.plot_tree(T, filled=True, feature_names=X.columns)

fig, ax = plt.subplots(1, figsize = (20, 20))
p = tree.plot_tree(T, filled = True, feature_names = X.columns)


