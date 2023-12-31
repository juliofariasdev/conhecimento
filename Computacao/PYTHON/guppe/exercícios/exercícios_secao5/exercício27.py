idade = int(input('Qual a idade do nadador: '))
if idade>=5 and idade<=7:
    print(f'Sua categoria é infantil A')
elif idade>=8 and idade<=10:
    print(f'Sua categoria é infantil B')
elif idade>=11 and idade<=13:
    print(f'Sua categoria é juvenil A')
elif idade>=14 and idade<=17:
    print(f'Sua categoria é juvenil B')
elif idade>17:
    print(f'Sua categoria é Sênior')
else:
    print('ERRO')