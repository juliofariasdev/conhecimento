matriz = [[(1*j) for j in range(3)] for i in range(3)]
soma =0
for i in range(3):
    for j in range(3):
        if (i+j) ==2:
            soma += matriz[i][j]
            break
print(matriz)
print(soma)