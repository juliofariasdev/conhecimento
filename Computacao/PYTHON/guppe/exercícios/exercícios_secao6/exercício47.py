n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while True:
    print(f'Qual operação você deseja realizar.')
    print(f'''Escolha uma opção:
    [1] - adição
    [2] - subtração
    [3] - multiplicação
    [4] - divisão 
    [5] - saída''')
    escolha = int(input(': '))
    if escolha==1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif escolha==2:
        print(f'{n1} - {n2} = {n1-n2}')
    elif escolha==3:
        print(f'{n1} * {n2} = {n1*n2}')
    elif escolha==4:
        print(f'{n1} / {n2} = {n1/n2}')
    elif escolha==5:
        print(f'FIM DO PRAGRAMA')
        break
    else:
        print(f'Opção inválida')