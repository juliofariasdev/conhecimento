n = int(input('Digite um número inteiro positivo: '))
c = n+1
while True:
    if c%11==0 or c%13==0 or c%17==0:
        break
    c+=1
print(f'{c} é o primeiro múltiplo de 11, 13 ou 17 após o {n}')