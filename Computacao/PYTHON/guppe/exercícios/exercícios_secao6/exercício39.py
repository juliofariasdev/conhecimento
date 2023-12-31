base = float(input('Qual a medida da base do seu triângulo, em metros: '))
altura = float(input('Qual a altura do seu triângulo, em metros: '))

if base>0 and altura>0:
    print(f'A área  do seu triângulo é {altura*base/2:.2f} metros quadrados')
else:
    print(f'Medidas inválidas')