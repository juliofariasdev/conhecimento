lista = []
v = int(input('Quantos números você quer que eu leia: '))
for i in range(v):
    lista.append(int(input(f'Digite o {i+1}º número inteiro: ')))
lista.sort()
lista.reverse()
print(f'O maior número inteiro digitado foi o {lista[0]} e apareceu {lista.count(lista[0])} vezes')