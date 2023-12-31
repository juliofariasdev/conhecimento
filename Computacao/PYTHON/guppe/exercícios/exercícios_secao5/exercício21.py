n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print(f'''Escolha a opção:
[1] para soma 
[2] para subtrair
[3] para multiplicar
[4] para dividir''')
resposta = str(input('Opção '))
if resposta=='1':
    print(n1+n2)
elif resposta=='2':
    if n1>n2:
        diferenca = n1-n2
    else:
        diferenca = n2-n1
    print(diferenca)
elif resposta=='3':
    print(n1*n2)
elif resposta=='4':
    if n2!=0:
        print(f'{n1/n2:.2f}')
    else:
        print(f'O denominador não pode ser zero!')
else:
    print(f'Opção inválida')