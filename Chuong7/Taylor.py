import numpy as np

def taylor_series_method(f, x0, y0, x_end, h, n):
    """
    f: Hàm số y' = f(x, y)
    x0: Giá trị ban đầu của x
    y0: Giá trị ban đầu của y
    x_end: Giá trị x cuối cùng mà ta muốn tính
    h: Bước nhảy
    n: Bậc của chuỗi Taylor
    """
    
    def compute_taylor_terms(f, x, y, h, n):
        terms = [y]
        y_derivative = y
        for i in range(1, n):
            y_derivative = f(x, y_derivative)
            term = (y_derivative * (h ** i)) / np.math.factorial(i)
            terms.append(term)
        return sum(terms)

    x_values = [x0]
    y_values = [y0]

    while x0 < x_end:
        y0 = compute_taylor_terms(f, x0, y0, h, n)
        x0 += h
        x_values.append(x0)
        y_values.append(y0)

    return x_values, y_values

# Ví dụ sử dụng:
# Phương trình vi phân y' = x + y với điều kiện ban đầu y(0) = 1

def f(t, y):
    # Định nghĩa hàm f(t, y) = dy/dt
    return 1+(t-y)**2

x0 = 2
y0 = 1
x_end = 3
h = 0.1
n = 4  # Bậc của chuỗi Taylor

x_values, y_values = taylor_series_method(f, x0, y0, x_end, h, n)

# In kết quả
for x, y in zip(x_values, y_values):
    print(f"x: {x:.2f}, y: {y:.4f}")
