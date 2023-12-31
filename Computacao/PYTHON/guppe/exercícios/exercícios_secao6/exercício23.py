n = int(input('Digite um número interio positivo: '))
print('Seu divisores', end=': ')
for i in range(1,n+1):
    if n % i ==0:
        print(i, end=' ')