def maior_valor(lista):
    maior = lista[0]
    for i in lista:
        if i > maior:
            maior =i
    return maior


print(maior_valor(list([1, 2, 3, 4, 1 ,2 ,3])))