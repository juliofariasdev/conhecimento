def soma_acima(matriz):
    soma =0
    for i in range(3):
        for j in range(3):
            if i<j:
                soma += matriz[i][j]
    return soma


A = [[i*j for j in range(3)]for i in range(3)]
print(soma_acima(A))