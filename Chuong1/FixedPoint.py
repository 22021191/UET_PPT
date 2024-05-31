import math
import decimal

# Ví dụ sử dụng
def g(x):
    return (2*(x**2) + 2*x - 1)**(1/3)# Phương trình 2*(x**2) + 2*x - 1)**(1/3)

p0 = 1  # Xấp xỉ ban đầu
TOL = 0.001  # Độ chính xác 10^-6
N0 = 100  # Số lần lặp tối đa

def fixed_point_iteration(g, p0, TOL, N0):
    """
    Tìm giải pháp xấp xỉ cho phương trình p = g(p)
    sử dụng phương pháp lặp điểm cố định
    
    Đầu vào:
    g: Hàm g(p) để tính xấp xỉ tiếp theo
    p0: Xấp xỉ ban đầu
    TOL: Độ chính xác mong muốn
    N0: Số lần lặp tối đa
    
    Đầu ra:
    Giải pháp xấp xỉ nếu thành công,
    hoặc thông báo thất bại nếu vượt quá số lần lặp tối đa
    """
    i = 1
    while i <= N0:
        
        p = g(p0)
        if abs(p - p0) < TOL:
            return p  # Đã tìm được nghiệm xấp xỉ
        i += 1
        p0 = p
    
    return f"The method failed after {N0} iterations, N0 = {N0}."

solution = fixed_point_iteration(g, p0, TOL, N0)
print(solution)
