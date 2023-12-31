altura = float(input("Qual a sua altura, em metros: "))
sexo = str(input("Qual o seu sexo, [F] ou [M]: "))
if sexo == 'F':
    peso_ideal = 62.1*altura -44.7
elif sexo =='M':
    peso_ideal = 72.7*altura -58
print(f'O seu peso ideal é {peso_ideal:.2f}')