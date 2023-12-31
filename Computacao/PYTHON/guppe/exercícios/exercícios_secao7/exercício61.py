def multiplicador_de_matrizes(matriz1, matriz2):
    matriz_transposta = [[matriz2[j][i] for j in range(3)]for i in range(3)]
    C = [[],[],[]]
    i =0
    for linha in matriz1:
        for coluna in matriz_transposta:
            soma = 0
            for m in list(zip(linha,coluna)):
                soma += m[0]*m[1]
            C[i].append(soma)
        i+=1
    return C


A = [
    [1,2,3],
    [2,4,6],
    [3,6,9]
]
B = [
    [4,5,6],
    [8,10,12],
    [12,15,18]
]
print(A)
print(B)
print(multiplicador_de_matrizes(A,B))