with open('exe9.txt') as arq1:
    texto1 = arq1.read()
with open('exe9-2.txt') as arq2:
    texto2 = arq2.read()
with open('exe9-3.txt', 'w') as arq3:
    arq3.write(texto1+texto2)