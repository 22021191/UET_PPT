import numpy as np

def power_method(A, num_iterations: int, tolerance: float):
    n, m = A.shape
    if n != m:
        raise ValueError("Matrix A must be square")
    
    # Start with a random vector
    b_k = np.random.rand(n)
    
    for _ in range(num_iterations):
        # Calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # Normalize the vector
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm
        
        # Check for convergence
        if np.linalg.norm(A @ b_k - b_k1_norm * b_k) < tolerance:
            break
    
    # Eigenvalue approximation
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)
    
    return eigenvalue, b_k

# Example usage
A = np.array([[4, 1], [2, 3]])
eigenvalue, eigenvector = power_method(A, num_iterations=1000, tolerance=1e-6)
print(f"Dominant Eigenvalue: {eigenvalue}")
print(f"Dominant Eigenvector: {eigenvector}")
