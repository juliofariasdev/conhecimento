n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
soma,produto = 0, 1
for i in range(n1, n2+1):
    if i % 2 == 0:
        soma += i
    else:
        produto *= i
print(f'A soma dos números pares no intervalo de {n1} a {n2} é {soma}')
print(f'O produto dos números ímpares no intervalo de {n1} a {n2} {produto}')