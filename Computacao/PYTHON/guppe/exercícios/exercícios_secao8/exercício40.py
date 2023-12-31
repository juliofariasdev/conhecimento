def valores_pares(lista):
    q =0
    for i in lista:
        if i%2==0:
            q +=1
    return q


print(valores_pares(list(range(10))))