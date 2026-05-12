import numpy as np

class Jacobi:
    def __init__(self, A, b):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)

    def convergencia(self, X_k1, X_k):
        return np.linalg.norm(X_k1 - X_k, ord=np.inf) / np.linalg.norm(X_k, ord=np.inf)

    def resolver(self, x_0 = None, max_iters = 100, p = 1e-6):
        A = self.A
        b = self.b
        n = len(A)
        k = 1

        x_k = x_0
        x_k1 = np.zeros(n)
        for j in range(n):
            x_k[j] = (1/A[j][j]) * (b[j] - np.sum(A[j][:j] * x_0[:j]) - np.sum(A[j][j+1:] * x_0[j+1:]))

        while k < max_iters:
            for j in range(n):

                fator = 1/A[j, j]
                x_k1[j] = fator * (b[j] - np.sum(A[j][:j] * x_k[:j]) - np.sum(A[j][j+1:] * x_k[j+1:]))

            k = k + 1
            x_k = x_k1

        self.x_k = x_k
        return self.x_k

    def imprimir(self):
        print(self.x_k)
