matriz = [[(i+j)  for j in range(3)] for i in range(3)]
soma =0
for i in range(3):
    for j in range(3):
        if i<j:
            soma+=matriz[i][j]
print(matriz)
print(soma)