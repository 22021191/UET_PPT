import numpy as np
import matplotlib.pyplot as plt

def divided_diff(x, y):
    """
    Tính bảng sai phân chia cho nội suy Newton.

    Tham số:
    x : list hoặc numpy array
        Danh sách các giá trị x của các điểm đã biết.
    y : list hoặc numpy array
        Danh sách các giá trị y của các điểm đã biết.

    Trả về:
    bảng sai phân chia.
    """
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:,0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i,j] = (diff_table[i+1,j-1] - diff_table[i,j-1]) / (x[i+j] - x[i])
    
    return diff_table

def newton_interpolation(x, y, xp):
    """
    Hàm thực hiện nội suy Newton.

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
    diff_table = divided_diff(x, y)
    n = len(x)
    yp = diff_table[0,0]
    product_term = 1.0

    for i in range(1, n):
        product_term *= (xp - x[i-1])
        yp += diff_table[0,i] * product_term
        print("a",i,"=",yp)
    return yp

# Ví dụ minh họa
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 1, 2, 3, 5])

# Giá trị cần nội suy
xp = 3.01

# Tính giá trị nội suy tại xp
yp = newton_interpolation(x, y, xp)

print(f"Giá trị nội suy tại x = {xp} là y = {yp}")

# Vẽ biểu đồ để minh họa
xp_vals = np.linspace(min(x), max(x), 100)
yp_vals = [newton_interpolation(x, y, i) for i in xp_vals]

plt.plot(x, y, 'o', label='Các điểm đã biết')
plt.plot(xp_vals, yp_vals, '-', label='Đường nội suy Newton')
plt.plot(xp, yp, 'ro', label=f'Nội suy tại x = {xp}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()