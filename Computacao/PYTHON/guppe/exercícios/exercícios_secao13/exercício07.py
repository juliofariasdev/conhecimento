with open('exe7.txt') as arq:
    texto = list(arq.read()).copy()
    vogais = 'aeiou'
    print(texto)
    for i in range(len(texto)):
        if texto[i] in vogais:
            texto[i] = '*'
with open('exe7.txt', 'w') as arq:
    arq.write(''.join(texto))