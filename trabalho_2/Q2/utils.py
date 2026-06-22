import os
import numpy as np
import sympy as sp
import pandas as pd

class NewtonBacktracking:
    def __init__(self, eps=1e-8, max_iters=80):
        self.eps = eps
        self.max_iters = max_iters
        self.x = sp.symbols('x')

    def calcular(self, xk, a, b, f):
        '''
        Aplica Newton com Backtracking e calcula as derivadas das funções 
        internamente.
        xk: chute inicial
        a: define exigencia para aceitar a proxima iteracao [0, 0.5]
        b: fator de contração. determina o quanto vai encurtar a proxima iteração [0, 1] 
        max_iters: numero maximo de iterações
        f: função a ser otimizada, deve ser declarada simbolicamente em x
        '''

        # Calcula derivada simbolica
        df = self.derivar(f)
        d2f = self.derivar(df)

        # Transforma em função calculável
        f = sp.lambdify(self.x, f)
        df = sp.lambdify(self.x, df)
        d2f = sp.lambdify(self.x, d2f)
        k = 0

        d2f_vec = []
        df_vec = []
        xk_vec = []
        f_vec = []

        while abs(df(xk)) > self.eps and k < self.max_iters:

            df_vec.append(abs(df(xk)))
            xk_vec.append(xk)
            f_vec.append(f(xk))
            d2f_vec.append(abs(d2f(xk)))

            if d2f(xk) > 0:
                vk = -df(xk)/d2f(xk)
            else:
                vk = -df(xk)

            while f(xk + vk) > (f(xk) + a*df(xk)*vk):
                vk = vk*b
            
            xk = xk + vk
            k+=1

            
            
        self.resultado = [xk_vec, df_vec, d2f_vec, f_vec]
        return self.resultado
    
    def derivar(self, f):
        return sp.diff(f, self.x)
    


    def imprimir(self, nome_arq):
        if self.resultado is None:
            self.calcular()

        
        tabela = pd.DataFrame(
            {
                'xk': self.resultado[0],
                'f(xk)': self.resultado[3],
                'modulo derivada': self.resultado[1],
                'modulo segunda derivada': self.resultado[2]
            }
        )
        tabela.index.name = 'iteração'
        print(tabela)
        
        print(f'xk:', self.resultado[0])
        print(f'modulo derivada:', self.resultado[1])

        print('\n')
        print('--------------------------------')
        print('\n')


        tabela.to_latex('../resultados_T2Q2/' + nome_arq + '.tex', index=True)