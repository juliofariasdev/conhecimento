matriz1, matriz2, matriz3= [[] for _ in range(4)], [[] for _ in range(4)], [[] for _ in range(4)]
for i in range(4):
    for j in range(4):
        matriz1[i].append(j + i)
        matriz2[i].append(j * i)
for i in range(4):
    for j in range(4):
        if matriz1[i][j]>=matriz2[i][j]:
            matriz3[i].append(matriz1[i][j])
        else:
            matriz3[i].append(matriz2[i][j])
print(matriz3)