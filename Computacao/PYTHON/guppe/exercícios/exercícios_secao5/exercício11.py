n = int(input('Digite um número inteiro positivo: '))
soma = 0
lista = [1, 2]
if n>0:
    for _, i in enumerate(str(n)):
        soma += int(i)
    print(f'A soma dos seus algarismos é {soma}')
else:
    print(f'Número inválido!')