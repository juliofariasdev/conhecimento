valor_do_produto = float(input('Qual o valor do produto: R$'))
estado = str(input('Qualo estado destino, em sigla: ')).upper()
if estado=='MG':
    valor_final = 1.07*valor_do_produto
    print(f'O valor final do produto é R${valor_final:.2f}')
elif estado=='SP':
    valor_final = 1.12*valor_do_produto
    print(f'O valor final do produto é R${valor_final:.2f}')
elif estado=='RJ':
    valor_final = 1.15*valor_do_produto
    print(f'O valor final do produto é R${valor_final:.2f}')
elif estado=='MS':
    valor_final =1.08*valor_do_produto
    print(f'O valor final do produto é R${valor_final:.2f}')
else:
    print(f'Estado inválido!')