import numpy as np
import sympy as sp


x = sp.symbols('x')

f = (sp.sqrt(x**2 + 4))/3 + (sp.sqrt((6-x)**2 + 9))/2

df = sp.diff(f, x)
d2f = sp.diff(df, x)

print(f)
print(df)
print(d2f)

## Se vocês usarem um ipynb da pra usar display(f) e fica bonitinho. deixei 
## um arquivo prontinho (dev.ipynk) ali com as funções bonitinhas. tem que instalar a biblioteca ipykernel pra rodar
