n = int(input('Digite um número inteiro maoir que 1: '))
i =None
for i in range(2,n+1):
    if n%i==0:
        break
if i ==n:
    print(f'{n} é primo')
else: print(f'{n} não é primo')