import numpy as np
import matplotlib.pyplot as plt

# Given data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Degree of the polynomial
degree = 2

# Create the Vandermonde matrix
V = np.vander(x, degree + 1, increasing=True)

# Solve the least squares problem
coefficients, residuals, rank, singular_values = np.linalg.lstsq(V, y, rcond=None)

# Print the coefficients
print("Coefficients:", coefficients)

# Evaluate the fitted polynomial
x_fit = np.linspace(min(x), max(x), 100)
V_fit = np.vander(x_fit, degree + 1, increasing=True)
y_fit = np.dot(V_fit, coefficients)
plt.scatter(x, y, label='Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
