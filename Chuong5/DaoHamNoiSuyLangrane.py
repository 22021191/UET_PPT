import numpy as np

def lagrange_basis(x, x_points, index):
    basis = 1
    for i, x_i in enumerate(x_points):
        if i != index:
            basis *= (x - x_i) / (x_points[index] - x_i)
    return basis

def finite_difference_derivative(x_points, y_points, x_eval, h=1e-5):
    n = len(x_points)
    
    # Nội suy để tìm giá trị của hàm tại x_eval
    y_eval = sum(y_points[i] * lagrange_basis(x_eval, x_points, i) for i in range(n))
    
    # Nội suy để tìm giá trị của hàm tại x_eval + h
    y_eval_h = sum(y_points[i] * lagrange_basis(x_eval + h, x_points, i) for i in range(n))
    
    # Tính đạo hàm theo phương pháp sai phân tiến
    derivative = (y_eval_h - y_eval) / h
    return derivative

# Ví dụ sử dụng
x_points = np.array([0, 1, 2])
y_points = np.array([1, 2, 0])

# Điểm chúng ta muốn tính gần đúng đạo hàm
x_eval = 1

# Tính đạo hàm gần đúng bằng phương pháp sai phân tiến
approx_deriv_finite_diff = finite_difference_derivative(x_points, y_points, x_eval)
print("Đạo hàm gần đúng bằng sai phân tiến tại x =", x_eval, "là", approx_deriv_finite_diff)
