def diagonal_principal(matriz):
    soma =0
    for i in range(3):
        for j in range(3):
            if i==j:
                soma += matriz[i][j]
    return soma


A = [[i*(1+j) for j in range(3)]for i in range(3)]
print(A)
print(diagonal_principal(A))