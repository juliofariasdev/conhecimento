n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Dgite outro número inteiro: '))
if n1>n2:
    print(f'{n1} é maior, a diferença entre eles é {n1-n2}')
elif n1<n2:
    print(f'{n2} é maior, a diferença entre eles é {n2-n1}')
else:
    print(f'Os números são iguais, a diferença entre eles é 0')