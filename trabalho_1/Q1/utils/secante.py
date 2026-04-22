import pandas as pd
import numpy as np


class Secante:
    def __init__(self, f, x0, x1, p = 1e-8, max_iters = 80):
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.p = p
        self.max_iters = max_iters
    
    def calcular(self):

        f = self.f
        x0 = self.x0
        x1 = self.x1
        p = self.p
        max_iters = self.max_iters


        x0_vec = []
        x1_vec = []
        func_vec = []
        digse_vec = []

        f0 = f(x0)
        f1 = f(x1)
        if abs(f1) > abs(f0):
            x0, x1 = x1, x0
            f0, f1 = f1, f0
        
        for k in range(max_iters):
            if abs(f1) < p:
                break
                #return (x1, k)
            
            s = f1/f0
            t = (x0 - x1)*s
            q = 1 - s

            if q == 0:
                return (None, k)
            
            x2 = x1 - t/q
            
            if abs(x1 - x0) < p*abs(x2):
                return x2, k
            f2 = f(x2)

            if abs(f2)>abs(f1):
                x0 = x2
                f0 = f2
            else:
                x0 = x1
                f0 = f1
                x1 = x2
                f1 = f2

            x0_vec.append(x0)
            x1_vec.append(x1)
            func_vec.append(f2)
            digse_vec.append(self._digse(x0,x1))
        

        return x0_vec, x1_vec, func_vec, digse_vec
        
    
    def imprimir(self):
        if self.resultado is None:
            self.calcular()

        tabela = pd.DataFrame(
            {
                'x0': self.resultado[0],
                'x1': self.resultado[1],
                'f(x1)': self.resultado[2],
                'DIGSE': self.resultado[3]
            }
        )
        tabela.index.name = 'iteração'
        print(tabela)
        print('\n')
        print('--------------------------------')
        print('\n')


        print(tabela)