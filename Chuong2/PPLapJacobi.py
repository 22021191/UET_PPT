import numpy as np

def jacobi_method(A, b, XO, TOL, N):
    n = len(b)
    x = np.zeros_like(b, dtype=np.double)
    k = 1

    while k <= N:
        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))
            sum2 = sum(A[i, j] * x[j] for j in range(i+1, n))
            
            x[i] = (b[i] - sum1-sum2 ) / A[i, i]

        if np.linalg.norm(x - XO) < TOL:
            print(f"Converged after {k} iterations")
            return x

        print("Lan Lap thu ",k,":",x)
        k += 1
        XO = x.copy()
    print("Maximum number of iterations exceeded")
    return x

# Example usage
n = 4
A = np.array([[10, -1, 2, 0],
              [-1, 11, -1, 3],
              [2, -1, 10, -1],
              [0, 3, -1, 8]], dtype=np.double)
b = np.array([6, 25, -11, 15], dtype=np.double)
XO = np.zeros(n, dtype=np.double)
TOL = 10**-9
N = 1000

solution = jacobi_method(A, b, XO, TOL, N)
print("Solution:", solution)
