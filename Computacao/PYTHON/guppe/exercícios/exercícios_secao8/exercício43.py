from random import randint

def aleatorio(lista):
    lista = list({randint(0,10) for i in range(10)})
    return lista


print(aleatorio([]))