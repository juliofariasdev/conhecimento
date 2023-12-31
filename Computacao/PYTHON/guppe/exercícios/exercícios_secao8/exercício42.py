def media(lista):
    quantidade = 0
    soma =0
    for i in lista:
        soma+=i
        quantidade +=1
    return soma/quantidade


print(media([1,2,3,4,5,6,7]))