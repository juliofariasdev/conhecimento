n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunada nota: '))
if (n1>=0 and n1<=10)and(n2>=0 and n2<=10):
    print(f'A média dessas notas é {(n1+n2)/2}')
else:
    print(f'Notas inválidas!')