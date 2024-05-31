import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, xp):
    """
    Hàm thực hiện nội suy Lagrange.

    Tham số:
    x : list hoặc numpy array
        Danh sách các giá trị x của các điểm đã biết.
    y : list hoặc numpy array
        Danh sách các giá trị y của các điểm đã biết.
    xp : float hoặc numpy array
        Giá trị x tại điểm cần nội suy.

    Trả về:
    yp : float hoặc numpy array
        Giá trị nội suy tại xp.
    """
    yp = 0.0
    n = len(x)
    
    for i in range(n):
        p = 1.0
        for j in range(n):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += p * y[i]
        
    return yp

# Ví dụ minh họa
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 0, 2, 1])

# Giá trị cần nội suy
xp = 2.5

# Tính giá trị nội suy tại xp
yp = lagrange_interpolation(x, y, xp)

print(f"Giá trị nội suy tại x = {xp} là y = {yp}")

# Vẽ biểu đồ để minh họa
xp_vals = np.linspace(min(x), max(x), 100)
yp_vals = [lagrange_interpolation(x, y, i) for i in xp_vals]

plt.plot(x, y, 'o', label='Các điểm đã biết')
plt.plot(xp_vals, yp_vals, '-', label='Đường nội suy Lagrange')
plt.plot(xp, yp, 'ro', label=f'Nội suy tại x = {xp}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
