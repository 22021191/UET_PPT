import numpy as np

def rayleigh_quotient_iteration(A, v, tol=1e-10, max_iterations=1000):
    """
    Phương pháp Rayleigh để tìm trị riêng và vector riêng của ma trận A.

    :param A: Ma trận vuông cần tìm trị riêng.
    :param v: Vector đầu vào ban đầu.
    :param tol: Ngưỡng hội tụ.
    :param max_iterations: Số lần lặp tối đa.
    :return: Trị riêng và vector riêng.
    """
    n = A.shape[0]
    I = np.eye(n)
    v = v / np.linalg.norm(v)  # Chuẩn hóa vector v
    mu = np.dot(v.T, np.dot(A, v))  # Tính trị riêng ban đầu
    
    for i in range(max_iterations):
        try:
            w = np.linalg.solve(A - mu * I, v)
        except np.linalg.LinAlgError:
            break
        v = w / np.linalg.norm(w)
        mu_new = np.dot(v.T, np.dot(A, v))
        
        if np.abs(mu_new - mu) < tol:
            break
        mu = mu_new
    
    return mu, v

# Ma trận A
A = np.array([[5, 1, 1],
              [1, 6, 1],
              [1, 1, 7]])

# Vector đầu vào (1, 0, 0)
v0_1 = np.array([1, 0, 0])
eigenvalue_1, eigenvector_1 = rayleigh_quotient_iteration(A, v0_1)
print(f"Trị riêng từ vector đầu vào (1, 0, 0): {eigenvalue_1}")
print(f"Vector riêng: {eigenvector_1}")

# Vector đầu vào (-1, 5, 1)
v0_2 = np.array([-1, 5, 1])
eigenvalue_2, eigenvector_2 = rayleigh_quotient_iteration(A, v0_2)
print(f"Trị riêng từ vector đầu vào (-1, 5, 1): {eigenvalue_2}")
print(f"Vector riêng: {eigenvector_2}")
