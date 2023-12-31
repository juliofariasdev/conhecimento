n = int(input('Digite um número inteiro: '))
v = 1
for i in range(1,n+1):
    for e in range(1,i+1):
        print(f'{v}', end=' ')
        v += 1
    print()