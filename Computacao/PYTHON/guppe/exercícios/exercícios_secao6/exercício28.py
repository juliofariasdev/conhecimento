import math

lista = []
n = int(input('Digite um número inteiro positivo: '))
c = 0
while c<=n:
    lista.append(1/math.factorial(c))
    c += 1
print(f'O valor de E é {sum(lista):.2f}')