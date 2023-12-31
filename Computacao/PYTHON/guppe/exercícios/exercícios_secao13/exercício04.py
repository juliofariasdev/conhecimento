with open('exe4.txt') as exe4:
    texto = exe4.read()
    conseantes = ('bcdfghjklmnpqrstvwxyz')
    quantidade = 0
    for letra in texto:
        if letra in conseantes:
            quantidade += 1
    print(f'o arquivo exe4.txt tem {quantidade} consoantes')