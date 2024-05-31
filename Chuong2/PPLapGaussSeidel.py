import numpy as np

def gauss_seidel(A, b, tolerance=1e-10, max_iterations=1000):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    
    # Initialize the array for the previous iteration values
    x_prev = np.zeros_like(x, dtype=np.double)

    for k in range(max_iterations):
        for i in range(n):
            sum_Ax = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x_prev[i + 1:])
            x[i] = (b[i] - sum_Ax) / A[i, i]

        # Check for convergence
        if np.linalg.norm(x - x_prev, ord=np.inf) < tolerance:
            print(f"Converged after {k + 1} iterations")
            return x

        x_prev = x.copy()

    print("Max iterations reached without convergence")
    return x

# Example usage
A = np.array([[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]], dtype=np.double)

b = np.array([4, 7, 3], dtype=np.double)

solution = gauss_seidel(A, b)
print("Solution:", solution)
