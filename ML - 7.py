import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

new_sample = pd.DataFrame(
    [[5.0, 3.6, 1.4, 0.2]],
    columns=iris.feature_names
)

prediction = classifier.predict(new_sample)
print(f"New sample prediction: {iris.target_names[prediction[0]]}")

