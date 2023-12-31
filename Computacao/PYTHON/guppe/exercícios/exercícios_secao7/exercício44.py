matriz =[[] for _ in range(5)]
x = 6
v = False
for i in range(5):
    for j in range(5):
        matriz[i].append(j+i)
for i in range(5):
    for j in range(5):
        if x==matriz[i][j]:
            break
    if x == matriz[i][j]:
        print(f'Valor encontrado na linha {i} e coluna {j}')
        v = True
        break
if v ==False:
    print('Valor não encontrado')