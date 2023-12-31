matriz = []
for c in range(4):
    matriz.append([])
for i in range(4):
    for j in range(4):
        matriz[i].append((1+i)*(j+1))
print(matriz)