n = int(input('Digite um número inteiro positivo: '))
lista = []
for i in range(1, n+1):
    lista.append(1/i)
print(f'O número harmônico em função de {n} é {sum(lista):.2f}')