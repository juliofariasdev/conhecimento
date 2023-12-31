n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
print(f'''[1] para soma 
[2] para subtrair
[3] para multiplicar
[4] para dividir''')
resposta = str(input('? '))
if resposta=='1':
    print(n1+n2)
elif resposta=='2':
    print(n1-n2)
elif resposta=='3':
    print(n1*n2)
elif resposta=='4':
    print(n1/n2)