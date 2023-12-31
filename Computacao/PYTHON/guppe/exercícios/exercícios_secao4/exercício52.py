inves1 = float(input('Quanto o primeiro amigo investiu: R$'))
inves2 = float(input('Quanto o segundo amigo investiu: R$'))
inves3 = float(input('Quanto o tercerio amigo investiu: R$'))
total_inves = inves3+inves2+inves1
valor_do_premio = float(input('Qual o valor do prêmio: R$'))
print(f'''O primeiro amigo receberá R${valor_do_premio*(inves1/total_inves)}
O segundo amigo receberá R${valor_do_premio*(inves2/total_inves)}
O tercerio amigo receberá R${valor_do_premio*(inves3/total_inves)}''')