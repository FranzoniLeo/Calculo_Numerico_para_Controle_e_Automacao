import numpy as np

A = np.array([
    [1, -1, 1, -1, 1],
    [1,  0, 0,  0, 0],
    [1,  1, 1,  1, 1]
])

b = np.array([
    [2],
    [1],
    [2]
])

AAT = A @ A.T
y = np.linalg.solve(AAT, b)
xLN = A.T @ y

print("xLN =")
print(xLN)

# Norma Euclidiana
norma = np.linalg.norm(xLN)

print("\n||xLN|| =")
print(norma)