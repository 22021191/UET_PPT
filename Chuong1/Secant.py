import math

def find_solution(f, p0, p1, tol, max_iter):
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i <= max_iter:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)  # Step 3: Tính p_i
        if abs(p - p1) < tol:  # Kiểm tra |p - p1| < TOL
            return p  
        
        i += 1  
        p0, q0, p1, q1 = p1, q1, p, f(p)  #Cập nhật p0, q0, p1, q1

    print(f"Phương pháp thất bại sau {max_iter} lần lặp.")  # Step 7
    return None  

# Example usage
def f(x):
    return x**3 - 2*x**2 - 2*x + 1  # Định nghĩa hàm f(x)

initial_approximations = [0, 1]  # giá trị xấp xỉ ban đầu 
tolerance = 1e-6  # độ chính xác mong muốn
max_iterations = 100  # số lần lặp tối đa

solution = find_solution(f, *initial_approximations, tolerance, max_iterations)
if solution is not None:
    print(f"Nghiệm xấp xỉ là: {solution}")