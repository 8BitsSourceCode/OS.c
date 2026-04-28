import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "Math":[85,58,95,45,76,62,90,55,82,70],
    "Physics":[78,65,88,50,80,70,92,60,85,68],
    "Chemistry":[92,60,91,55,72,68,95,58,88,72],
    "Passed":["Yes","No","Yes","No","Yes","No","Yes","No","Yes","Yes"]
})

X = data[["Math","Physics","Chemistry"]].values
y = LabelEncoder().fit_transform(data["Passed"].values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train:", y_train)
print("y_test:", y_test)
