matriz = [
    [int(input('Qual a matricula do aluno')) for i in range(5)],
    [int(input('Qual a média das provas')) for i in range(5)],
    [int(input('Qual a média dos trabalhos')) for i in range(5)]
]
matriz.append([(matriz[1][i]+matriz[2][i])/2 for i in range(5)])
print(matriz)
for indice, valor in enumerate(matriz[3]):
    if max(matriz[3]) == valor:
        m = indice+1
        break
print(f'A matrícula do aluno que obteve a maior nota final é {m}')
print(f'A média dos alunos é {sum(matriz[3])}')