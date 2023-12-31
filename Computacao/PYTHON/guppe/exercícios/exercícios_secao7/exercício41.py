matriz = []
for c in range(5):
    matriz.append([])
for i in range(5):
    for j in range(5):
        if i ==j:
            matriz[i].append(1)
        else:
            matriz[i].append(0)
print(matriz)
