lista = []
c=1
while c<11:
    n = int(input(f'Digite o {c}º número: '))
    c+=1
    lista.append(n)
lista.sort()
lista.reverse()
print(f'O menor número lido é {lista[len(lista)-1]} e o maior é {lista[0]}')