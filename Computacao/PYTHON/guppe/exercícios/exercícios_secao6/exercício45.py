print(f'Converssor de velocidade')
while True:
    print('Escolha uma opção: ')
    print(f'[A] Converter Km/h para m/s')
    print(f'[B] converter m/s para Km/s')
    print(f'[C] Finalizar o programa')
    escolha = str(input(': ')).upper()
    if escolha == "A":
        velocidade = float(input('Qual a velocidade, em Km/h: '))
        print(f'{velocidade}Km/h corresponde a {velocidade/3.6:.2f}m/s')
    elif escolha == 'B':
        velocidade = float(input('Qual a velocidade, em m/s: '))
        print(f'{velocidade}m/s corresponde a {velocidade*3.6:.2f}Km/s')
    elif escolha =='C':
        print(f'Programa finalizado')
        break
    else:
        print(f'Opção inválida')