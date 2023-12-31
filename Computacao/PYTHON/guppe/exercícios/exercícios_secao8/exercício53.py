def identidade(matriz):
    verificacao1 = False
    verificacao2 = False
    ordem = len(matriz)
    for i in range(ordem):
        for j in range(ordem):
            if i==j and matriz[i][j]==1:
                verificacao1 = True
            elif i!=j and matriz[i][j]==0:
                verificacao2 = True
    if verificacao1 is True and verificacao2 is True:
        return f'É matriz identidade'
    return f'Não é matriz identidade'


A = [[1 if j==i else 0 for j in range(4)]for i in range(4)]
print(A)
print(identidade(A))