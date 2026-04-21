import numpy as np

L1 = [5, 3, 4]
L2 = [3, 1, 7]
L3 = [2, 1, 3]

b = [5, 3, 2]

A = np.vstack((L1, L2, L3)).astype(float)


def gauss(A, b):
    b = np.array(b)
    b = b.reshape(-1, 1) # vetor coluna
    Ab = np.hstack((A, b)).astype(float)

    for i in range(Ab.shape[1] - 1):
        pivot = Ab[i, i]
        Ab[i] = Ab[i]/pivot
        for j in range(i + 1, Ab.shape[0]):  
            aux = Ab[i]*Ab[j, i]
            Ab[j] = Ab[j] - aux

    return Ab, Ab[:, -1]

Ab, solucao = gauss(A, b)


