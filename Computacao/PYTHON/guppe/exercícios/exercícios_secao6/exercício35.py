n1 = int(input('Digite o valor inicial: '))
n2 = int(input('Digite o valor final: '))
lista = []

if n1<n2:
    for i in range(n1, n2+1):
        if i%2!=0:
            lista.append(i)
    print(f'A soma dos números ímpares neste intervalo é {sum(lista)}')
else:

    print(f'intervalo inválido!')