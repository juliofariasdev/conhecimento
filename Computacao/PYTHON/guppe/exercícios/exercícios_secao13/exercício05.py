with open('exe5.txt') as arq:
    texto = arq.read()
    char = input('Digite um caracter: ')
    quantidade = texto.count(char)
    print(f'o carecter "{char}" aparece {quantidade} vezes')