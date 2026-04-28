# Step 1: Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Step 2: Create dataset inside program
data = {
    "UserID": [15624510,15810944,15668575,15603246,15804002,15728773,15598044,15694829,15600575,
               15727311,15570769,15606274,15746139,15704987,15628972,15697686,15733883,15617482,15704583],
    
    "Gender": ["Male","Male","Female","Female","Male","Male","Female","Female","Male",
               "Female","Female","Female","Male","Male","Male","Male","Male","Male","Male"],
    
    "Age": [19,35,26,27,19,27,27,32,25,35,26,26,20,32,18,29,47,45,46],
    
    "EstimatedSalary": [19000,20000,43000,57000,76000,58000,84000,150000,33000,
                        65000,80000,52000,86000,18000,82000,80000,25000,26000,28000],
    
    "Purchased": [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Preprocessing
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])  # Male=1, Female=0

# Features and Target
X = df[['Gender', 'Age', 'EstimatedSalary']]
y = df['Purchased']

# Step 4: Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 5: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Prediction
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("Predicted values:", y_pred)
print("Actual values:", y_test.values)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))