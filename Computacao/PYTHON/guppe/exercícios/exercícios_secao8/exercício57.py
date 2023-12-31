def soma_coluna(matriz,n=1):
    soma =0
    for i in matriz:
        soma +=i[n]
    return soma


A = [[j for j in range(4)]for i in range(4)]
print(A)
print(soma_coluna(A))