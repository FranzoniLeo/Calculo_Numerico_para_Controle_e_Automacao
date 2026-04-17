import numpy as np
import pandas as pd


def funcao(f, eps = 0.0002, D = 0.05, Re = 100000):
    return ((1/(np.sqrt(f))) + (2*np.log10(((eps)/(3.7*D)) + ((2.51)/(Re*(np.sqrt(f)))))))


def funcao_derivada(f, eps = 0.0002, D = 0.05, Re = 100000):
    termo1 = -(1/(2*(f**(3/2))))
    termo2 = 2/np.log(10)
    termo3a = -(2.51/(2*Re*f**(3/2)))
    termo3b = (eps/(3.7*D)) + (2.51/(Re*np.sqrt(f)))
    return termo1 + (termo2 * (termo3a/termo3b))


def digse(xa, xd):
    return -(np.log10((abs(xd - xa))/(abs(xd))))


def bisseccao(f, a, b, p = 1e-8, max_iters = 80):

    xa_vec = []
    xs_vec = []
    func_vec = []
    digse_vec = []

    xa = a
    xb = b
    i = 1
    xs = (xa + xb)/2
    while (i < max_iters) and (digse(xa, xs) < -np.log10(p)):
        if (f(xs)*f(xa))<0:
            xb = xs
        else:
            xa = xs
        xs = (xa + xb)/2
        i = i + 1

        xa_vec.append(xa)
        xs_vec.append(xs)
        func_vec.append(f(xs))
        digse_vec.append(digse(xa,xs))

    return xa_vec, xs_vec, func_vec, digse_vec


def falsa_posicao(f, a, b, p = 1e-8, max_iters = 80):

    xa_vec = []
    xs_vec = []
    func_vec = []
    digse_vec = []

    x1 = a
    x2 = b 
    f1 = f(x1)
    f2 = f(x2) 

    xa = a
    xb = b

    i = 1
    xs = x1 - (x2 - x1)*f1/(f2 - f1)
    while (i < max_iters) and (digse(xa, xs) < -np.log10(p)):
        fs = f(xs)
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
        func_vec.append(f(xs))
        digse_vec.append(digse(xa,xs))

    return xa_vec, xs_vec, func_vec, digse_vec


def newton(f, df, x0, p = 1e-8, max_iters = 80):

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
        digse_vec.append(digse(x0,x1))

        x0 = x1
        i = i + 1

    return xk_vec, func_vec, dfunc_vec, digse_vec


def secante(f, x0, x1, p = 1e-8, max_iters = 80):

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
        digse_vec.append(digse(x0,x1))
    
    return x0_vec, x1_vec, func_vec, digse_vec
        



resultado_falsa_posicao = falsa_posicao(funcao, 0.01, 0.10)
#print(resultado_falsa_posicao[0], resultado_falsa_posicao[1], resultado_falsa_posicao[2], resultado_falsa_posicao[3], resultado_falsa_posicao[4])

resultado_bissecção = bisseccao(funcao, 0.01, 0.10)
#print(resultado_bissecção[0], resultado_bissecção[1], resultado_bissecção[2], resultado_bissecção[3], resultado_bissecção[4])

resultado_newton = newton(funcao, funcao_derivada, 0.01)
#print(resultado_newton[0], resultado_newton[1], resultado_newton[2], resultado_newton[3], resultado_newton[4])

resultado_secante = secante(funcao, 0.02, 0.05)
#print(resultado_secante[0], resultado_secante[1], resultado_secante[2], resultado_secante[3], resultado_secante[4])

tabela_bissecção = pd.DataFrame(
    {
        'xa': resultado_bissecção[0],
        'xs': resultado_bissecção[1],
        'função(xs)': resultado_bissecção[2],
        'digse(xa,xs)': resultado_bissecção[3],
    }
)
tabela_bissecção.index.name = 'iteração'
print(tabela_bissecção)
print('\n')
print('--------------------------------')
print('\n')



tabela_falsa_posicao = pd.DataFrame(
    {
        'xa': resultado_falsa_posicao[0],
        'xs': resultado_falsa_posicao[1],
        'função(xs)': resultado_falsa_posicao[2],
        'digse(xa,xs)': resultado_falsa_posicao[3],
    }
)
tabela_falsa_posicao.index.name = 'iteração'
print(tabela_falsa_posicao)
print('\n')
print('--------------------------------')
print('\n')


tabela_newton = pd.DataFrame(
    {
        'xk': resultado_newton[0],
        'função(xk)': resultado_newton[1],
        'dfunção(xk)': resultado_newton[2],
        'digse(x0,xk)': resultado_newton[3],
    }
)
tabela_newton.index.name = 'iteração'
print(tabela_newton)
print('\n')
print('--------------------------------')
print('\n')


tabela_secante = pd.DataFrame(
    {
        'x0': resultado_secante[0],
        'x1': resultado_secante[1],
        'função(x1)': resultado_secante[2],
        'digse(x0,x1)': resultado_secante[3],
    }
)
tabela_secante.index.name = 'iteração'
print(tabela_secante)
print('\n')
print('--------------------------------')
print('\n')

