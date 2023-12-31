preco_antigo = float(input('Qual o preço antigo: R$'))
preco_novo =0
if preco_antigo<=50:
    preco_novo = preco_antigo*1.05
elif preco_antigo>50 and preco_antigo<=100:
    preco_novo = preco_antigo*1.1
elif preco_antigo>100:
    preco_novo = preco_antigo*1.15
print(f'R${preco_novo:.2f}')
if preco_novo<=80:
    print(f'Barato')
elif preco_novo>80 and preco_novo<=120:
    print(f'Normal')
elif preco_novo>120 and preco_novo<=200:
    print(f'Caro')
elif preco_novo>200:
    print('Muito caro')
