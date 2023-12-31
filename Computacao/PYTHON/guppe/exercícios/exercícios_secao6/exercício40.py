lista = []
n = 1
while True:
    n = int(input('Digite um número: '))
    if n>0:
        lista.append(n)
    else:
        break
print(f'O maior número lido foi {max(lista)} e menor foi {min(lista)}')
