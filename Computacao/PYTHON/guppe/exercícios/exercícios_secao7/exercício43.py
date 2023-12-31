matriz = []
linha = None
coluna = None
for _ in range(4):
    matriz.append([])
for i in range(4):
    for j in range(4):
        matriz[i].append(i+j)
maior = matriz[0][0]
for i in range(4):
    for j in range(4):
        if matriz[i][j]> maior:
            maior=matriz[i][j]
            coluna =j
            linha=i
print(f'O maior valor é {maior} e se encontrar na \nlinha {linha} e coluna {coluna}')