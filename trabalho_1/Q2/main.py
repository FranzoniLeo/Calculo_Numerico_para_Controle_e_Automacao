from utils.gauss import Gauss
from utils.LUP import LUP
from utils.Jacobi import Jacobi
import numpy as np

A = [[4, -1, 0, -1, 0, 0, 0, 0, 0],
     [-1, 4, -1, 0, -1, 0, 0, 0, 0],
     [0, -1, 4, 0, 0, -1, 0, 0, 0],
     [-1, 0, 0, 4, -1, 0, -1, 0, 0],
     [0, -1, 0, -1, 4, -1, 0, -1, 0],
     [0, 0, -1, 0, -1, 4, 0, 0, -1],
     [0, 0, 0, -1, 0, 0, 4, -1, 0],
     [0, 0, 0, 0, -1, 0, -1, 4, -1],
     [0, 0, 0, 0, 0, -1, 0, -1, 4],]

b = [175, 100, 150, 75, 0, 50, 75, 0, 50]


gauss = Gauss(A, b)
gauss.triangularizacao()
gauss.retrosubstituicao()
gauss.imprimir()

lup = LUP(A, b)
lup.fatoracaoLUP()
lup.resolver()
lup.imprimir()


jacobi = Jacobi(A, b)
jacobi.resolver(x_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0])
jacobi.imprimir()