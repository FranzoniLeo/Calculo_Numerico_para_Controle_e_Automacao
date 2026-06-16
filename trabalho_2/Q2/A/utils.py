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
        while abs(df(xk)) > self.eps and k < self.max_iters:
            if d2f(xk) > 0:
                vk = -df(xk)/d2f(xk)
            else:
                vk = -df(xk)

            while f(xk + vk) > (f(xk) + a*df(xk)*vk):
                vk = vk*b
            
            xk = xk + vk
            k+=1
        self.resultado = [xk, abs(df(xk)), k]
        return self.resultado
    
    def derivar(self, f):
        return sp.diff(f, self.x)
    


    def imprimir(self):
        if self.resultado is None:
            self.calcular()

        '''
        tabela = pd.DataFrame(
            {
                'xk': self.resultado[0],
                'modulo derivada': self.resultado[1],
                'iteração': self.resultado[2],
            }
        )
        tabela.index.name = 'iteração'
        print(tabela)
        '''
        print(f'xk:', self.resultado[0])
        print(f'modulo derivada:', self.resultado[1])
        print(f'iteração:', self.resultado[2])

        print('\n')
        print('--------------------------------')
        print('\n')