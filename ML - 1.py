import numpy as np

# Given arrays
X = np.array([10, 20, 30, 40, 50])
Y = np.array([5, 15, 25, 35, 45])

# a) Expected Value (same as mean for equal probability)
expected_value = np.mean(X)
print("Expected Value:", expected_value)

# b) Mean
mean_X = np.mean(X)
mean_Y = np.mean(Y)
print("Mean of X:", mean_X)
print("Mean of Y:", mean_Y)

# c) Standard Deviation
std_X = np.std(X)
std_Y = np.std(Y)
print("Standard Deviation of X:", std_X)
print("Standard Deviation of Y:", std_Y)

# d) Variance
var_X = np.var(X)
var_Y = np.var(Y)
print("Variance of X:", var_X)
print("Variance of Y:", var_Y)

# e) Covariance
covariance = np.cov(X, Y)[0][1]
print("Covariance between X and Y:", covariance)

# f) Covariance Matrix
cov_matrix = np.cov(X, Y)
print("Covariance Matrix:\n", cov_matrix)
