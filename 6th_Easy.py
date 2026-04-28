import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.DataFrame({
'User ID':[15624510,15810944,15668575,15603246,15804002,15728773,15598044,15694829,15600575,15727311,15570769,15606274,15746139,15704987,15628972,15697686,15733883,15617482,15704583],
'Gender':['Male','Male','Female','Female','Male','Male','Female','Female','Male','Female','Female','Female','Male','Male','Male','Male','Male','Male','Male'],
'Age':[19,35,26,27,19,27,27,32,25,35,26,26,20,32,18,29,47,45,46],
'EstimatedSalary':[19000,20000,43000,57000,76000,58000,84000,150000,33000,65000,80000,52000,86000,18000,82000,80000,25000,26000,28000],
'Purchased':[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1]
})
data = data.drop("User ID", axis=1)
data['Gender'] = data['Gender'].map({'Male': 1, ' ;Female': 0})

X = data[['Age', 'EstimatedSalary']]
y = data['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print(cm)
print(accuracy)
