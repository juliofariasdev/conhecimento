with open('exe8.txt') as arq:
    texto = arq.read()
with open('exe8-2.txt', 'w') as arq:
    arq.write(texto.upper())