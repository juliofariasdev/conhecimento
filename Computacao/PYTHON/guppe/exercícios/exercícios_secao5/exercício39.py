salario_atual = float(input('Qual o seu salário atual: R$'))
tempo_de_servico = int(input('Tempo de serviço, em anos: '))
bonus, reajuste = 0,1
if salario_atual<=500:
    reajuste +=0.25
elif salario_atual>500 and reajuste<=1000:
    reajuste +=0.2
elif salario_atual>1000 and reajuste<=1500:
    reajuste +=0.15
elif salario_atual>1500 and reajuste<=2000:
    reajuste +=0.1
elif salario_atual>2000:
    reajuste = 0
if tempo_de_servico>=1 and tempo_de_servico<=3:
    bonus += 100
elif tempo_de_servico>=4 and tempo_de_servico<=6:
    bonus += 200
elif tempo_de_servico>=7 and tempo_de_servico<=10:
    bonus += 300
elif tempo_de_servico>10:
    bonus +=500
if salario_atual!=salario_atual*reajuste+bonus:
    print(f'Seu salário atual é R${salario_atual*reajuste+bonus:.2f}')
else:
    print(f'Seu salário atual continua o mesmo R${salario_atual:.2f}')