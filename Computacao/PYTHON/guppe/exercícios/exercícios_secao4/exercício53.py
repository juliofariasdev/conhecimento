comprimento = float(input('Qual o comprimento do seu terreno, em metro: '))
largura = float(input('Qual a largura do seu terreno, em metro: '))
perimetro = 2*comprimento+2*largura
preco_da_tela = float(input('Qual o preço do metro de tela: R$'))
print(f'O custo para cercar este mesmo \nterreno com tela é R${perimetro/preco_da_tela:.2f}')