def diagonal_secundária(matriz):
    return sum([sum([matriz[i][j] if i+j==2 else 0 for j in range(3)]) for i in range(3)])


A = [[(10*j*i) for j in range(3)] for i in range(3)]
print(A)
print(diagonal_secundária(A))