with open('exe6.txt') as arq:
    texto = arq.read()

    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    for char in alfabeto:
        vezes = texto.count(char)
        print(f'{char} aparece {vezes} no arquivo')