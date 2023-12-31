peso = float(input('Qual o seu peso, em kg: '))
altura = float(input('Qual a sua altura, em metro: '))
imc = peso/altura**2
print(f'seu IMC {imc} e é ', end='')
if imc<18.5:
    print(f'Abaixo do Peso')
elif imc>=18.5 and imc<25:
    print('Saudável')
elif imc>=25 and imc<30:
    print('Peso em excesso')
elif imc>=30 and imc<35:
    print('Obesidade grau I')
elif imc>=35 and imc<40:
    print(f'Obesidade grau II')
elif imc>=40:
    print(f'Obesidade grau III')