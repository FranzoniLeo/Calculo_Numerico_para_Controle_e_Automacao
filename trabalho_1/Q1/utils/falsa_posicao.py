import numpy as np
import pandas as pd

class FalsaPosicao:
    

    def __init__(self, f, a, b, p = 1e-8, max_iters = 80):
        self.f = f
        self.a = a
        self.b = b
        self.p = p
        self.max_iters = max_iters
    
    def _digse(self, xa, xd):
        return -(np.log10((abs(xd - xa)) / (abs(xd))))

    def calcular(self):

        xa_vec = []
        xs_vec = []
        func_vec = []
        digse_vec = []

        x1 = self.a
        x2 = self.b
        f1 = self.f(x1)
        f2 = self.f(x2)

        xa = self.a
        xb = self.b

        i = 1
        xs = x1 - (x2 - x1)*f1/(f2 - f1)
        while (i < self.max_iters) and (self._digse(xa, xs) < -np.log10(self.p)):
            fs = self.f(xs)
            if (fs*f1)<0:
                x2 = xs
                f2 = fs
            else:
                x1 = xs
                f1 = fs
            xa = xs
            xs = x1 - ((x2 - x1)*f1)/(f2 - f1)
            i = i + 1

            xa_vec.append(xa)
            xs_vec.append(xs)
            func_vec.append(self.f(xs))
            digse_vec.append(self._digse(xa,xs))

        return xa_vec, xs_vec, func_vec, digse_vec

    def imprimir(self):
        if self.resultado is None:
            self.calcular()

        tabela = pd.DataFrame(
            {
                'xa': self.resultado[0],
                'xs': self.resultado[1],
                'função(xs)': self.resultado[2],
                'digse(xa,xs)': self.resultado[3],
            }
        )
        tabela.index.name = 'iteração'
        print(tabela)
        print('\n')
        print('--------------------------------')
        print('\n')