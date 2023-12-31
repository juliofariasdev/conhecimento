n1 = int(input('Digite um número: '))
n2 = int(input('Digite outor número: '))
n3 = int(input('Digite mais um número: '))
lista = [n1,n2,n3]
lista.sort()
for _, n in enumerate(lista):
    print(f"{n}", end=' ')