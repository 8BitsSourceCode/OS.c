# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Step 2: Dataset (inside program)
data = {
    'Age': [25,35,45,20,35,52,23,40,60,48,33,28,50,37,29],
    'Income': ['Low','Low','High','Low','High','High','Low','High','High','High','Low','Low','High','High','Low'],
    'Student': ['No','No','No','Yes','Yes','No','Yes','Yes','No','Yes','No','Yes','No','Yes','Yes'],
    'Credit_Rating': ['Fair','Excellent','Fair','Fair','Excellent','Excellent','Fair','Fair','Excellent','Fair','Fair','Excellent','Excellent','Fair','Fair'],
    'Buys_Computer': ['No','No','Yes','Yes','Yes','No','Yes','Yes','No','Yes','No','Yes','No','Yes','Yes']
}

df = pd.DataFrame(data)

# Step 3: Encode categorical data
le = LabelEncoder()
for col in ['Income','Student','Credit_Rating','Buys_Computer']:
    df[col] = le.fit_transform(df[col])

# Step 4: Split data
X = df.iloc[:, :-1]
y = df['Buys_Computer']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Step 5: Train model
model = RandomForestClassifier(n_estimators=50, random_state=0)
model.fit(X_train, y_train)

# Step 6: Prediction
y_pred = model.predict(X_test)

# Step 7: Evaluation metrics
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

# Step 8: Predict new sample
sample = pd.DataFrame([[30,1,1,1]], columns=X.columns)
pred = model.predict(sample)

print("Prediction (Buys Computer):", "Yes" if pred[0]==1 else "No")