# Step 1: Import libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 2: Load dataset
iris = load_iris()
X = iris.data        # features
y = iris.target      # labels

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 4: Create KNN model (k = 3)
model = KNeighborsClassifier(n_neighbors=3)

# Step 5: Train model
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 8: Predict new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
print("Prediction:", iris.target_names[model.predict(sample)[0]])