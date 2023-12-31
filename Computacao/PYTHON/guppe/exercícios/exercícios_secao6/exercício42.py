while True:
    n = int(input('Digite um número: '))
    if n>0:
        print(f'O quadrado de {n} vale {n**2}')
        print(f'O cubo de {n} vale {n**3}')
        print(f'A raiz quadrada de {n} vale {n**0.5:.2f}')
    else:
        print(f'FIM')
        break