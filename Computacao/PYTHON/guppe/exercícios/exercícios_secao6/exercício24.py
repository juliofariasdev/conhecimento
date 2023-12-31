n = int(input('Digite um número inteiro positivo: '))
lista = []
c = 1
while c<n:
    if n % c == 0:
        lista.append(c)
    c +=1
print(f'{sum(lista)} é a soma de todos os divisores de {n}')