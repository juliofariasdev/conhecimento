salario = float(input('Qual o seu salário: R$'))
valor_da_prestaçao = float(input('Qual o valor da prestação do empréstimo: R$'))
if valor_da_prestaçao<= 0.2*salario:
    print(f'Empréstimo concedido')
else:
    print(f'Empréstimo não concedido')