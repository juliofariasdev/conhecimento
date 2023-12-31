def principal_and_segundaria(matriz):
    ordem = len(matriz)
    soma= 0
    for i in range(ordem):
        for j in range(ordem):
            if j==i or j+i==ordem-1:
                soma+=matriz[i][j]
    return soma


A = [[i for j in range(4)] for i in range(4)]
print(A)
print(principal_and_segundaria(A))