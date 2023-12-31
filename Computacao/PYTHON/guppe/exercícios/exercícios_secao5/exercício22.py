idade = int(input('Qual a sua idade: '))
tempo_de_servico = int(input('Tempo de serviço: '))
if idade>=65 or tempo_de_servico>=30 or (idade>=60 and tempo_de_servico>=25):
    print(f'Esse trabalhador pode se aposentar.')
else:
    print(f'Esse trabalhador não pode se aposentar.')