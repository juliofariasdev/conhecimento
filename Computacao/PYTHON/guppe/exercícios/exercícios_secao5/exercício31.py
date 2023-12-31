altura = float(input('Qual a sua altura: '))
peso = float(input('Qual a seu peso, kg: '))
print(f'A classificação dessa pessoa é', end=' ')
if altura<1.20:
    if peso<=60:
        print('A')
    elif peso>60 and peso<=90:
        print('D')
    elif peso>90:
        print('G')
elif altura>1.20 and altura<=1.70:
    if peso<=60:
        print('B')
    elif peso>60 and peso<=90:
        print('E')
    elif peso>90:
        print('H')
elif altura>1.70:
    if peso<=60:
        print('C')
    elif peso>60 and peso<=90:
        print('F')
    elif peso>90:
        print('I')
print(f'Fim do programa')
