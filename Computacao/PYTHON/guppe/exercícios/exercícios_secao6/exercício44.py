n = int(input('Digite um número inteiro: '))
lista = [0, 1, 1]
while True:
    print(lista[0])
    if lista[0] > n:
        break
    lista[0] = lista[1]
    lista[1] = lista[2]
    lista[2] = lista[0]+lista[1]
