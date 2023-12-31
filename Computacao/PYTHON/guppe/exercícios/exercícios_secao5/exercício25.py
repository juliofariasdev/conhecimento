a = float(input('Qual o valor do coeficiente a: '))
b = float(input('Qual o valor do coeficiente b: '))
c = float(input('Qual o valor do coeficiente c: '))
if a!=0:
    delta = b**2 -4*a*c
    if delta<0:
        print(f'Para delta negativo, não existe raizes reais>')
    elif delta==0:
        raiz =(-b+ delta**0.5)/(2*a)
        print(f'Para delta nulo, existe raiz única, {raiz}')
    elif delta>0:
        raiz1 = (-b + delta ** 0.5) / (2 * a)
        raiz2 = (-b - delta ** 0.5) / (2 * a)
        print(f'Para delta positivo, existe duais raizes reais, {raiz1} e {raiz2}')
else:
    print(f'Não é uma equação do segundo grau')