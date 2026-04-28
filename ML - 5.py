import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Generate 100 data points
np.random.seed(42)  # for reproducibility
X = np.arange(1, 101).reshape(-1, 1)

# Add noise to create ups and downs
noise = np.random.normal(0, 2000, size=X.shape[0])
y = (X.flatten()**2) + noise

# Polynomial transformation
poly = PolynomialFeatures(degree=10)
X_poly = poly.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_poly, y)

# Predictions
y_pred = model.predict(X_poly)

# Plot
plt.figure(figsize=(8,5))
plt.scatter(X, y, color='blue', label='Noisy Data', s=15)
plt.plot(X, y_pred, color='red', label='Polynomial Fit', linewidth=2)
plt.title('Polynomial Regression with Noise (Ups & Downs)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
