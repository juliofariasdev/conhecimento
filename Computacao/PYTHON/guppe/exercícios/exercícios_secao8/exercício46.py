def impressao_normal(lista):
    print(lista)


def impressao_inversa(lista=list):
    lista.reverse()
    print(lista)


def media(lista):
    return sum(lista)/len(lista)


impressao_normal(list(range(10)))
impressao_inversa(list(range(10)))
print(media(list(range(10))))
