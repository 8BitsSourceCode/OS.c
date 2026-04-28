import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'Experience': [1,2,3,4,5,6,7,8,9,10],
    'Salary': [30000,35000,40000,45000,50000,55000,60000,65000,70000,75000]
}

df = pd.DataFrame(data)
X = df[['Experience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
comparison = pd.DataFrame({'Actual Salary': y_test.values, 'Predicted Salary': y_pred})
print(comparison)

plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train, model.predict(X_train), color='red')
plt.title("Training Set (Experience vs Salary)")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test, y_test, color='green')
plt.plot(X_train, model.predict(X_train), color='red')
plt.title("Testing Set (Experience vs Salary)")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
