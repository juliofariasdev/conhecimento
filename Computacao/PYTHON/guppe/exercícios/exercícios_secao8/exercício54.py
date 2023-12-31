soma = lambda matriz: sum([sum(i) for i in matriz])

A = [[i for j in range(5)]for i in range(5)]

print(soma(A))