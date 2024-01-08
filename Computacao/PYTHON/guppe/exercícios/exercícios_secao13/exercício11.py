nome_do_arquivo = input('Digite o nome do arquivo: ')
palavra = input('Digite um nome de palavra: ')

with open(nome_do_arquivo) as file:
    text = file.read()
    words = text.split()
quantidades = words.count(palavra)
print(f'No arquivo {nome_do_arquivo} contém {quantidades} vezes a palavra {palavra}')