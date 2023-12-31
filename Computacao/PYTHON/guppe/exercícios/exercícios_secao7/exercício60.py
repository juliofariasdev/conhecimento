def somador_de_matriz(matriz1,matriz2):
    C = [[]for i in range(2)]
    for i in range(2):
        for j in range(2):
            C[i].append(matriz1[i][j]+ matriz2[i][j])
    return C


def subtrador_de_matriz(matriz1, matriz2):
    C = [[] for i in range(2)]
    for i in range(2):
        for j in range(2):
            C[i].append(matriz1[i][j] - matriz2[i][j])
    return C


def adicionador_de_constante(matriz1, matriz2,constante):
    for i in range(2):
        for j in range(2):
            matriz1[i][j] += constante
            matriz2[i][j] += constante
    return matriz1, matriz2


A = [
    [5, 7],
    [6, 8]
]
B = [
    [1, 3],
    [2, 4]
]
K = 10
escolha = input(f'''opçõs: 
[a] soma as duas matrizes
[b] subtrair as duas matrizes
[c] adiciona uma constante ás duas matrizes
escolha:''')
if escolha=='a':
    print(somador_de_matriz(A,B))
elif escolha=='b':
    print(subtrador_de_matriz(A,B))
elif escolha=='c':
    print(adicionador_de_constante(A,B,K))
else:
    print("ERRO!")