from min_quad import MinimosQuadrados

x_treino = [-2.0000, -1.7143, -1.4286, -1.1429,
            -0.8571, -0.5714, -0.2857, 0.0000]

y_treino = [9.5728, 7.8761, 5.9407, 3.6790,
            3.5833, 2.3987, 1.1968, 1.2906]

x_teste = [0.0000, 0.6667, 1.3333, 2.0000]

y_teste = [1.1823, 1.0137, 2.0809, 4.8734]

for grau in [1, 2, 3, 4]:

    mq = MinimosQuadrados(x_treino, y_treino, grau)

    mq.imprimir()
    #mq.exportar()

    # calcula teste aqui fora
    mse_te = mq.MSE_teste(x_teste, y_teste)
    print(f"MSE teste = {mse_te:.6f}")