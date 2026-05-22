import numpy as np
import pandas as pd

'''
Limitações:
Sem pivoteamento: se A[i, i] == 0 (ou quase zero), há divisão por zero (ou instabilidade). Algoritmos robustos trocam linhas (pivoteamento parcial).
'''

class Gauss:
    def __init__(self, A, b):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)

    def triangularizacao(self):
        n = len(self.A)

        for i in range(n): #colunas
            for j in range(i + 1, n):#linhas
                pivot = self.A[j, i]
                diagonal = self.A[i, i]
                #print(pivot, diagonal)
                factor = pivot / diagonal 
                for k in range(i, n):
                    self.A[j, k] -= factor * self.A[i, k] #aplicar o  fator a linha j
                self.b[j] -= factor * self.b[i] #aplicar o fator ao b

    def retrosubstituicao(self):
        n = len(self.A)
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            soma = 0.0
            for j in range(i + 1, n):
                soma += self.A[i, j] * x[j]
            # x[i] = (b[i] - soma) / A[i,i]
            x[i] = (self.b[i] - soma) / self.A[i, i]

        self.resultado = x
        return self.resultado

    def imprimir(self):
        print(" ")
        print(self.resultado)


    def exportar(self):
        if self.resultado is None:
            self.triangularizacao()
            self.retrosubstituicao()

        tabela = pd.DataFrame(
            {
                'x': self.resultado
            }
        )
        tabela.index.name = 'iteração'
        
        tabela.to_latex('trabalho_1/Q2/resultados_Q2/elimgauss_Q2.tex', index=True)

        pass