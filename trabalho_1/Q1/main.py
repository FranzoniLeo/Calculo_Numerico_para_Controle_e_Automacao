import numpy as np


from utils.bisseccao import Bisseccao

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


bisseccao = Bisseccao(funcao, 0.01, 0.10)

bisseccao.calcular()
bisseccao.imprimir()

