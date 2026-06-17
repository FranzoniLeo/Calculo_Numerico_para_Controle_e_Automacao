import numpy as np
import pandas as pd

class MinimosQuadrados:

    def __init__(self, x, y, grau):

        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.grau = grau

        self.A = self.matriz_A()
        self.cLS = self.calcular()


    def matriz_A(self):
        A = np.zeros((len(self.x), self.grau + 1))
        for i in range(self.grau + 1):
            A[:, i] = self.x**i
        return A

    def calcular(self):

        A = self.A
        b = self.y

        cLS = np.linalg.inv(A.T @ A) @ A.T @ b

        return cLS
    
    def y_pred(self):

        return self.A @ self.cLS #multiplica as matrizes  
    
    def MSE(self):

        y_pred = self.y_pred()
        mse = np.mean((self.y - y_pred)**2)

        return mse

    def imprimir(self):
        #print("Matriz A:")
        #print(self.A)
        print(f"\nPolinômio de grau {self.grau}")
        print("cLS =")
        print(self.cLS)

        print(f"MSE treino = {self.MSE():.6f}")

    def exportar(self):

        tabela = pd.DataFrame(
            {
                f'c{i}': [self.cLS[i]]
                for i in range(len(self.cLS))
            }
        )

        tabela.to_latex(
            f'resultado_grau_{self.grau}.tex',
            index=False
        )

        return tabela