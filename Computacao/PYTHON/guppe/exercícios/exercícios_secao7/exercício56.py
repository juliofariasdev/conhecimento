notas = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 3, 3],
    [5, 4, 6],
    [9, 10, 1],
    [3, 3, 3],
    [5, 4, 6],
    [9, 10, 1],
    [1, 2, 3],
    [3, 2, 1],
]
n1=0
n2=0
n3=0
for i in range(10):
    for indice,valor in enumerate(notas[i]):
        if min(notas[i])==valor:
            if indice==0:
                n1+=1
            elif indice==1:
                n2+=1
            else:
                n3+=1
            break
print(f'O número de alunos cuja pior nota foi na prova 1 é {n1}')
print(f'O número de alunos cuja pior nota foi na prova 2 é {n2}')
print(f'O número de alunos cuja pior nota foi na prova 3 é {n3}')