transpostador_de_matriz = lambda matriz: [[matriz[j][i] for j in range(len(matriz))]for i in range(len(matriz[0]))]
def soma_das_colunas_impares(matriz):
    matriz_transposta = transpostador_de_matriz(matriz)
    indice = 1
    soma = 0
    for coluna in matriz_transposta:
        if indice%2:
            soma = sum(coluna, soma)
        indice +=1
    return soma


def media_aritmetica_da_segunda_e_quarta_coluna(matriz):
    matriz_transposta = transpostador_de_matriz(matriz)
    return sum(matriz_transposta[1],sum(matriz_transposta[3]))


def substitui_sexta_pela_soma_1_e_2(matriz):
    matriz_transposta = transpostador_de_matriz(matriz)
    nova_coluna = [sum(par) for par in list(zip(matriz_transposta[0], matriz_transposta[1]))]
    matriz_transposta[5] = nova_coluna
    matriz_nova = transpostador_de_matriz(matriz_transposta)
    return  matriz_nova


A = [
    [1, 3, 5, 7, 9, 11],
    [2, 4, 6, 8, 10, 12],
    [2, 3, 5, 7, 11, 17]
]
print(A)
print(soma_das_colunas_impares(A))
print(media_aritmetica_da_segunda_e_quarta_coluna(A))
print(substitui_sexta_pela_soma_1_e_2(A))