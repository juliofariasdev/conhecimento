"""
Escrevendo em arquivos


# OBS: Ao abrir um arquivos para leitura, não podemos realizar a escrita nele. Apenas ler.
De mesma forma , se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.
Caso o arquivo já exista, será apagado e criado um novo no lugar.

with open('nome_do_arquivo.extensao', 'w') as apelido: -> será criado um arquivo para escrita.
    contexto de trabalho

arquivo.write('texto') -> escreve o 'texto' no arquivo.
"""