soma = lambda matriz, n=1: sum(matriz[n])

A = [[i for j in range(6)]for i in range(7)]
print(A)
print(soma(A))