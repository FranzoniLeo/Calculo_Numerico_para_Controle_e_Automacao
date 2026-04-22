import pandas as pd
import numpy as np


class Newton:
    ''' Inicialização da classe Newton
    Args:
        f: Função a ser analisada
        df: Derivada da função f
        x0: Ponto inicial
        p: Precisão (padrão: 1e-8)
        max_iters: Número máximo de iterações (padrão: 80)
    '''
    def __init__(self, f, df, x0, p = 1e-8, max_iters = 80):
        self.f = f
        self.df = df
        self.x0 = x0
        self.p = p
        self.max_iters = max_iters
    
    def _digse(self, xa, xd):
        return -(np.log10((abs(xd - xa)) / (abs(xd))))

    def calcular(self):
        f = self.f
        df = self.df
        x0 = self.x0
        p = self.p
        max_iters = self.max_iters

        xk_vec = []
        func_vec = []
        dfunc_vec = []
        digse_vec = []

        i = 0 

        gf = f(x0)
        dgf = df(x0)
        if dgf == 0:
            return None, i
        x1 = x0 - (gf/dgf)

        while (i < max_iters):
            gf = f(x0)
            dgf = df(x0)

            if dgf == 0:
                return None, i
            
            x1 = x0 - (gf/dgf)
            if abs(f(x1)) < p:
                return xk_vec, func_vec, dfunc_vec, digse_vec


            xk_vec.append(x1)
            func_vec.append(f(x1))
            dfunc_vec.append(df(x1))
            digse_vec.append(self._digse(x0,x1))

            x0 = x1
            i = i + 1

        self.resultado = (xk_vec, func_vec, dfunc_vec, digse_vec)
        return self.resultado 
        
    

    def imprimir(self):
        if self.resultado is None:
            self.calcular()

        tabela = pd.DataFrame(
            {
                'xk': self.resultado[0],
                'f(xk)': self.resultado[1],
                'df(xk)': self.resultado[2],
                'digse': self.resultado[3]
            }
        )

        tabela.index.name = 'iteração'
        print(tabela)
        print('\n')
        print('--------------------------------')
        print('\n')