def diagonal_4(matriz):
    matrizT = [[matriz[j][i]for j in range(20)]for i in range(20)]


A = [[i*j for j in range(1, 21)]for i in range(1,21)]
[print(i)for i in A]
diagonal_4(A)