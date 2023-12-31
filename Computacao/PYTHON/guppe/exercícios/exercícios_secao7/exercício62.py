def quadrado_de_uma_matriz(matriz1):
    ordem = len(matriz1)
    matriz_transposta = [[matriz1[j][i] for j in range(ordem)]for i in range(ordem)]
    C = [[] for _ in range(ordem)]
    i =0
    for linha in matriz1:
        for coluna in matriz_transposta:
            soma = 0
            for m in list(zip(linha,coluna)):
                soma += m[0]*m[1]
            C[i].append(soma)
        i+=1
        if i== ordem:
            break
    return C


A = [
    [1,2],
    [4,3]
]
print(quadrado_de_uma_matriz(A))