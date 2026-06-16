from utils import NewtonBacktracking
import sympy as sp


n_backtrack = NewtonBacktracking()

x = n_backtrack.x
f = (sp.sqrt(x**2 + 4))/3 + (sp.sqrt((6-x)**2 + 9))/2
n_backtrack.calcular(xk=1.0, a=0.5, b=0.9, f=f)
n_backtrack.imprimir()