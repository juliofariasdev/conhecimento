n = int(input('Digite um número inteiro: '))
if ((n%5==0)or(n%3==0))and not(n%5==0 and n%3==0):
    if (n%5==0):
        print(f'Esse número é divísevel por 5')
    else:
        print(f'Esse número é divisível por 3')
else:
    print(f'Número inválido!')
