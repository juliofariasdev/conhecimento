with open('exe10.txt') as arq:
    print()
    linhas = arq.readlines()
    maior = 0
    cidade = None
    for linha in linhas:
        if int(linha.split(' ')[-1])>=maior:
            maior = int(linha.split(' ')[-1])
            cidade = ' '.join(linha.split(' ')[0:-1])
with open('exe10-2.txt', 'w') as arq2:
    arq2.write(f'a cidade mais populosa e {cidade} com {maior} habitantes')