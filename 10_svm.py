# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Step 2: Dataset (inside program)
data = {
    'Age': [22,25,47,52,46,56,27,30,40,48],
    'Income': ['Low','Low','High','High','High','High','Low','Low','High','High'],
    'Student': ['No','No','No','No','Yes','Yes','Yes','No','Yes','Yes'],
    'Buys': ['No','No','Yes','Yes','Yes','Yes','No','No','Yes','Yes']
}

df = pd.DataFrame(data)

# Step 3: Encode categorical data
le = LabelEncoder()
for col in ['Income','Student','Buys']:
    df[col] = le.fit_transform(df[col])

# Step 4: Split data
X = df.iloc[:, :-1]
y = df['Buys']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Step 5: Train SVM model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Step 6: Prediction
y_pred = model.predict(X_test)

# Step 7: Evaluation metrics
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

# Step 8: Predict new sample
sample = pd.DataFrame([[30,1,1]], columns=X.columns)
pred = model.predict(sample)

print("Prediction (Buys):", "Yes" if pred[0]==1 else "No")