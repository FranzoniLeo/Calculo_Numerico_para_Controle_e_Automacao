import matplotlib.pyplot as plt
from min_quad import MinimosQuadrados

x_treino = [-2.0000, -1.7143, -1.4286, -1.1429,
            -0.8571, -0.5714, -0.2857, 0.0000]

y_treino = [9.5728, 7.8761, 5.9407, 3.6790,
            3.5833, 2.3987, 1.1968, 1.2906]

x_teste = [0.0000, 0.6667, 1.3333, 2.0000]

y_teste = [1.1823, 1.0137, 2.0809, 4.8734]

# Para plot do gráfico
graus =[]
mse_treino = []
mse_teste = []

for grau in [1, 2, 3, 4]:

    mq = MinimosQuadrados(x_treino, y_treino, grau)
    
    graus.append(grau)
    mse_treino.append(mq.MSE())
    mse_teste.append(mq.MSE_teste(x_teste, y_teste))
    
    mq.imprimir()
    mq.exportar()

    # Calcula teste aqui 
    mse_te = mq.MSE_teste(x_teste, y_teste)
    print(f"MSE teste = {mse_te:.6f}")


# Plota gráfico de MSE vs grau do polinômio
plt.plot(graus, mse_treino, marker='o', label='Treino')
plt.plot(graus, mse_teste, marker='o', label='Teste')

plt.xlabel('Grau do polinômio')
plt.ylabel('Erro Quadrático Médio (MSE)')
plt.title('Erro Quadrático Médio em função do grau do polinômio')
plt.legend()
plt.grid(True)

plt.savefig("mse_grau.png", dpi=300, bbox_inches='tight')
plt.show()
