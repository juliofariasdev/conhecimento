"""
Sistema de Arquivos e Navegação

Para  fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os

os -> Operating Sistem - Sistema Operacional

os.getcwd() -> pega o diretório de trabalho atual, retornando path absoluto dele

path (windows) - Unidade:\\User\\User_name\\... = caminho

os.chdir('path_absoluto') -> muda o diretório atual de trabalho

os.chdir('..') -> volta pro diretório anterior até chegar na unidade

os.path.isabs() -> verifica se o path é absoluto

os.name -> retorna qual é o SO usado

os.path.jain(path_absoluto,path_relativo) -> junta path realivo oa absoluto.

os.listdir(path) = lista o que tem no diretório revelente ao path

arquivos = list(os.scandir(path)) = lista o que tem no diretório revelente ao path com mais detalhe

arquivo = arquivos[0]

arquivo.path -> busca o path do arquivo

arquivo.stat() -> informarções do arquivo

"""
import os

os.chdir('..')
novo = os.path.join(os.getcwd(),'exercícios', 'exercícios_secao5')
arq = list(os.scandir(novo))
print(arq[0].stat())
print(arq[0].name)
print(arq[0].inode())
print(arq[0].path)
print(arq[0].is_file())
print(arq[0].__class__)
print(arq[0].stat())