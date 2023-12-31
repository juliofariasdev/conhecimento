r1 = 0
r2 = 0
while True:
    r1 =float(input('Qual o valor do resistor R1: '))
    r2 =float(input('Qual o valor do resistor R2: '))
    if r1>0 and r2>0:
        R = (r1*r2)/(r1+r2)
        print(f'A associação em paralelo desses resistores é {R} ')
    else:
        print('ERRO')
        break