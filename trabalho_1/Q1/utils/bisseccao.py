import numpy as np
import pandas as pd


class Bisseccao:

    ''' Inicialização da classe Bisseccao 
    Args:
        f: Função a ser analisada
        a: Limite esquerdo do intervalo
        b: Limite direito do intervalo
        p: Precisão (padrão: 1e-8)
        max_iters: Número máximo de iterações (padrão: 80)
    '''
    def __init__(self, f, a, b, p=1e-8, max_iters=80):
        self.f = f
        self.a = a
        self.b = b
        self.p = p
        self.max_iters = max_iters
        self.resultado = None


    
    def _digse(self, xa, xd):
        return -(np.log10((abs(xd - xa)) / (abs(xd))))


    def calcular(self):
        f = self.f
        a = self.a
        b = self.b
        p = self.p
        max_iters = self.max_iters

        xa_vec = []
        xs_vec = []
        func_vec = []
        digse_vec = []

        xa = a
        xb = b
        i = 1
        xs = (xa + xb) / 2
        while (i < max_iters) and (self._digse(xa, xs) < -np.log10(p)):
            if (f(xs) * f(xa)) < 0:
                xb = xs
            else:
                xa = xs
            xs = (xa + xb) / 2
            i = i + 1

            xa_vec.append(xa)
            xs_vec.append(xs)
            func_vec.append(f(xs))
            digse_vec.append(self._digse(xa, xs))

        self.resultado = (xa_vec, xs_vec, func_vec, digse_vec)
        return self.resultado

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
