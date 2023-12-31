with open('arq.txt', 'a') as arq:
    texto = input('Digite um texto: ')
    for letra in texto:
        if letra=='0':
            break
        arq.write(letra)