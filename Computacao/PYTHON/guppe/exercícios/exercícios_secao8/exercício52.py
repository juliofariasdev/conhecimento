def quadrada(matriz):
    ordem = len(matriz)
    B = [[matriz[j][i] for j in range(ordem)]for i in range(ordem)]
    return B


A = [[i for j in range(5)]for i in range(5)]
print(A)
print(quadrada(A))