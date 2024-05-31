import numpy as np

def divided_differences(x, y):
    """Tính các hiệu chia tiến của Newton."""
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    return coef

def newton_polynomial(coef, x_data, x):
    """Tính giá trị của đa thức nội suy Newton tại x."""
    n = len(coef)
    p = coef[0]
    for k in range(1, n):
        p = coef[k] + (x - x_data[k - 1]) * p
    return p

def newton_polynomial_derivative(coef, x_data, x):
    """Tính đạo hàm của đa thức nội suy Newton tại x."""
    n = len(coef)
    derivative = 0
    for k in range(1, n):
        term = coef[k]
        for j in range(k - 1):
            term *= (x - x_data[j])
        derivative += term
    return derivative

# Dữ liệu đầu vào: các điểm (x, y)
x_data = np.array([0, 1, 2])
y_data = np.array([1, 2, 0])

# Tính các hệ số của đa thức nội suy Newton
coef = divided_differences(x_data, y_data)[0, :]

# Điểm mà chúng ta muốn tính gần đúng đạo hàm
x_eval = 1

# Tính đạo hàm gần đúng
approx_deriv_newton = newton_polynomial_derivative(coef, x_data, x_eval)
print("Đạo hàm gần đúng tại x =", x_eval, "là", approx_deriv_newton)
