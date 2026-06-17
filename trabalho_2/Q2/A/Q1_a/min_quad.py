import numpy as np
import pandas as pd

class MinimosQuadrados:

    def __init__(self, x, y, grau):

        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.grau = grau

        self.A = self.matriz_A()
        self.CLS = self.calcular()


    def matriz_A(self):
        A = np.zeros((len(self.x), self.grau + 1))
        for i in range(self.grau + 1):
            A[:, i] = self.x**i
        return A

    def calcular(self):

        A = self.A
        b = self.y

        CLS = np.linalg.inv(A.T @ A) @ A.T @ b

        return CLS
    
    def y_pred(self):

        return self.A @ self.CLS #multiplica as matrizes  
    
    def MSE(self):

        y_pred = self.y_pred()
        mse = np.mean((self.y - y_pred)**2)

        return mse
    
    def MSE_teste(self, x_teste, y_teste):

        x_teste = np.array(x_teste, dtype=float)
        y_teste = np.array(y_teste, dtype=float)

        A_te = np.zeros((len(x_teste), self.grau + 1))

        for i in range(self.grau + 1):
            A_te[:, i] = x_teste**i

        y_pred = A_te @ self.CLS

        mse = np.mean((y_teste - y_pred)**2)

        return mse

    def imprimir(self):
        #print("Matriz A:")
        #print(self.A)
        print(f"\nPolinômio de grau {self.grau}")
        print("cLS =")
        print(self.CLS)
        print(f"MSE treino: {self.MSE()}")
        

    def exportar(self):

        tabela = pd.DataFrame(
            {
                f'c{i}': [self.CLS[i]]
                for i in range(len(self.CLS))
            }
        )

        tabela.to_latex(
            f'resultado_grau_{self.grau}.tex',
            index=False
        )

        return tabela