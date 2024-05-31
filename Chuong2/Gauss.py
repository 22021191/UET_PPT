import numpy as np

def gauss_elimination(A, b):
    n = len(A)
    # Augmenting matrix A with vector b
    Ab = np.hstack((A, b.reshape(-1, 1)))

    # Forward elimination
    for k in range(n):
        # Find the pivot row
        m = k + np.argmax(np.abs(Ab[k:n, k]))  # maximum value in column k starting from row k
        if np.abs(Ab[m, k]) < 1e-12:  # considering floating-point tolerance
            return "No unique solution exists"

        # Swap the current row with the pivot row
        if m != k:
            Ab[[k, m]] = Ab[[m, k]]

        # Make the elements below the pivot in column k zero
        for j in range(k + 1, n):
            m_jk = Ab[j, k] / Ab[k, k]
            Ab[j, k:] -= m_jk * Ab[k, k:]

    # Check for no unique solution
    if np.any(np.abs(Ab[np.arange(n), np.arange(n)]) < 1e-12):
        return "No unique solution exists"

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]

    return x

# Example usage
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

solution = gauss_elimination(A, b)
print("Solution:", solution)
