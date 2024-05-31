import math

def find_solution(f, p0, tol, max_iter):
    i = 1
    
    while i <= max_iter:
        p = p0 - f(p0) / f_prime(p0)  # Cập nhật giá trị x theo công thức Newton-Raphson
        if abs(p - p0) < tol:  #Kiểm tra nếu |p - p0| < TOL
            return p 
        
        i += 1  
        p0 = p  
    print(f"The method failed after {max_iter} iterations.")  
    return None  # Quá trình không thành công

# Ví dụ sử dụng
def f(x):
    return x**3 - 2*x**2 - 2*x + 1  #  hàm số fx=x**3 - 2*x**2 - 2*x + 1
def f_prime(x):
    return 3*x**2 - 4*x - 2  # đạo hàm của hàm số fx

initial_approximation = 1  # giá trị sấp xỉ ban đầu
tolerance = 1e-6  # sai số cho phép 
max_iterations = 100  # số lần lặp tối đa 

solution = find_solution(f, initial_approximation, tolerance, max_iterations)
if solution is not None:
    print(f"Nghiệm xấp xỉ là : {solution}")