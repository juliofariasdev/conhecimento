soma =0
lista = [0,1,1]
while lista[0] <= 4000000:
    if lista[0]%2==0:
        soma+= lista[0]
    lista[0] = lista[1]
    lista[1] = lista[2]
    lista[2] = lista[0] + lista[1]
print(f'A soma dos valores pares \nda sequência de Fibonacci é {soma}')