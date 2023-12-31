with open('exe3.txt') as exe3:
    texto = exe3.read()
    vogais = ('a', 'e', 'i', 'o', 'u')
    quantidade = 0
    for letra in texto:
        if letra in vogais:
            quantidade += 1
    print(f'o arquivo exe3.txt tem {quantidade} vogais')