import numpy as np
import sympy as sp
import pandas as pd


class Jacobiana:
    def __init__(self, Fq, Q, h = 1e-6):
        self.Fq = Fq
        self.Q = np.array(Q, dtype=float)
        self.h = h
        self.determinar()
        self.J = self.calcular(self.Q)


    def determinar(self):
        Q1, Q2, Q3, Q4, Q5, Q6 = sp.symbols('Q1 Q2 Q3 Q4 Q5 Q6')
        Q = sp.Matrix([Q1,Q2,Q3,Q4,Q5,Q6])

        F = sp.Matrix([
            Q1 - 10,
            Q1 - Q2 - Q3,
            Q2 - Q4 - Q6,
            Q3 + Q4 - Q5,
            Q2**2 + Q4**2 - 4*Q3**2,
            Q4**2 + Q5**2 - 4*Q6**2
        ])

        J = F.jacobian(Q)
        sp.pprint(J)


    def calcular(self, Q):
        Fx = self.Fx
        h = self.h

        J = np.zeros((len(Fx(Q)), len(Q)))

        for i in range(len(Q)):
            dx = np.zeros(len(Q))
            dx[i] = h
            J[:, i] = (Fx(Q + dx) - Fx(Q)) / h

        self.J = J
        return self.J
        

    def Fx(self, Q):
        Q1, Q2, Q3, Q4, Q5, Q6 = Q

        return np.array([
            Q1 - 10,
            Q1 - Q2 - Q3,
            Q2 - Q4 - Q6,
            Q3 + Q4 - Q5,
            Q2**2 + Q4**2 - 4*Q3**2,
            Q4**2 + Q5**2 - 4*Q6**2
        ])

    def convergencia(self, Xk, Xk1):
        return np.linalg.norm(Xk1 - Xk, ord=np.inf)

    def resolver(self, max_iters = 100, p = 1e-8):
        Fx = self.Fx

        Xk = self.Q.copy()
        Xk1 = Xk + 2 * p
        k = 0
        
        convergencia_vec = []
        fx_vec = []
        xk_vec = []

        while (k < max_iters) and (self.convergencia(Xk, Xk1) > p):
            if k > 0:
                Xk = Xk1

            J = self.calcular(Xk)

            delta = np.linalg.solve(J, Fx(Xk))
            Xk1 = Xk - delta

            k = k + 1
            
            
            convergencia_vec.append(self.convergencia(Xk, Xk1))
            fx_vec.append(np.linalg.norm(Fx(Xk1), ord=np.inf))
            xk_vec.append(Xk)
    
        
        
        

        self.x_k1 = Xk1
        self.resultado = (xk_vec, fx_vec, convergencia_vec)
        return self.x_k1


    def imprimir(self):
        print(" ")
        print(self.x_k1)
        print(" ")  
        print(self.Fx(self.x_k1))



    def exportar(self):
        if self.resultado is None:
            self.resolver()
        tabela = pd.DataFrame(
            {
                'Q1': np.array(self.resultado[0])[:, 0],
                'Q2': np.array(self.resultado[0])[:, 1],
                'Q3': np.array(self.resultado[0])[:, 2],
                'Q4': np.array(self.resultado[0])[:, 3],
                'Q5': np.array(self.resultado[0])[:, 4],
                'Q6': np.array(self.resultado[0])[:, 5],
                '||f(x)||': self.resultado[1],
                'convergencia': self.resultado[2]
            }
        )
        tabela.index.name = 'iteração'
        tabela.to_latex('trabalho_1/Q3/resultados_Q3/jacobiana_resultado.tex', index=True)

        pass