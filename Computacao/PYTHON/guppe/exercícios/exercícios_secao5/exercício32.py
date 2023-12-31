print(f'''lanche     Código
Cachorro Quente         100
Bauru Simples           101
Bauru com Ovo           102
Hamburguer              103
CheeseBurguer           104
Suco                    105
Refrigerante            106
''')
codigo_do_produto = str(input('Qual o código do produto: '))
quantidade = int(input('Quantidade: '))
preco = 0
if codigo_do_produto=="100":
    preco = 1.2
elif codigo_do_produto=="101":
    preco = 1.3
elif codigo_do_produto=="102":
    preco = 1.5
elif codigo_do_produto=='103':
    preco = 1.2
elif codigo_do_produto=="104":
    preco = 1.7
elif codigo_do_produto=="105":
    preco = 2.2
elif codigo_do_produto=='106':
    preco = 1.0
print(f'O preço total é R${preco*quantidade:.2f}')