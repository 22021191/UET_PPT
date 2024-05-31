import numpy as np
import matplotlib.pyplot as plt

def cubic_spline_interpolation(x, y, t):
    n = len(x) - 1
    h = np.diff(x)
    alpha = np.zeros(n)
    
    for i in range(1, n):
        alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])

    l = np.ones(n+1)
    mu = np.zeros(n)
    z = np.zeros(n+1)
    c = np.zeros(n+1)
    b = np.zeros(n)
    d = np.zeros(n)

    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y[j+1] - y[j])/h[j] - h[j] * (c[j+1] + 2*c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3*h[j])

    def spline(t_val):
        for i in range(n):
            if x[i] <= t_val <= x[i+1]:
                dx = t_val - x[i]
                return y[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
        return None

    spline_values = np.array([spline(ti) for ti in t])
    return spline_values

# Dữ liệu đầu vào: các điểm (x, y)
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 1, 2, 3, 5])

# Tạo một dãy x mịn để vẽ spline
t = np.linspace(0, 9, 100)
y_interp = cubic_spline_interpolation(x, y, t)

# Vẽ dữ liệu gốc và spline
plt.figure()
plt.plot(x, y, 'o', label='Dữ liệu gốc')
plt.plot(t, y_interp, '-', label='Spline nội suy')
plt.legend()
plt.show()
