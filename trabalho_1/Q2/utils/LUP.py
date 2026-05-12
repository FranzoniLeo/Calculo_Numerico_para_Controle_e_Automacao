import numpy as np


class LUP:
    def __init__(self, A, b):
        self.A = np.array(A, dtype=float, copy=True)
        self.b = np.array(b, dtype=float, copy=True)
        self.p = None
        self.x = None
        self.u = None
        self.l = None

    def fatoracaoLUP(self):
        A = self.A
        n = len(A)

        p = np.arange(n, dtype=int)
        z = np.arange(n, dtype=int)

        for k in range(n - 1):
            for i in range(k, n):
                z[i] = A[p[i]][k]
            pos = k + int(np.argmax(np.abs(z[k:n])))

            p[k], p[pos] = p[pos], p[k]

            for i in range(k + 1, n):
                A[p[i]][k] = A[p[i]][k] / A[p[k]][k]
                mult = A[p[i]][k]

                for j in range(k + 1, n):
                    A[p[i]][j] = A[p[i]][j] - mult * A[p[k]][j]

        #print(A)            

        self.p = p
        return self

    def resolver(self):
        A = self.A
        p = self.p
        b = self.b

        n = len(A)
        l = np.zeros((n, n))
        u = np.zeros((n, n))
        permut = np.zeros((n, n))

        for i in range(n):
            permut[i, p[i]] = 1
        
        for i in range(n):
            for j in range(n):
                if j < i:
                    l[i, j] = A[p[i], j]
                elif j == i:
                    l[i, j] = 1.0
                    u[i, j] = A[p[i], j]
                else:
                    u[i, j] = A[p[i], j]

        #resultado1 = np.dot(permut, A)
        #resultado2 = np.dot(l, u)

        #print(resultado1)
        #print(resultado2)

        #print(p)

        #p_inv = np.linalg.inv(p)
        #resultado3 =np.dot(p_inv, l, u)

        u_inv = np.linalg.inv(u)
        l_inv = np.linalg.inv(l)

        x = np.dot(u_inv, np.dot(l_inv, np.dot(permut, b)))

        #print(x)

        self.x = x
        return self.x

    def imprimir(self):
        print(" ")
        print(self.x)