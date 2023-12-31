"""
PEP8 - Python Enhacement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia do PEP8 é que possamos escrever códigos de forma Pythônica.

[1] - utilize Camel case para nomes de classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass

[2] - utilize nomes em minúsculo, separados por undirlene para funções e variáveis

def soma():
    pass

def soma_dois():
    pass

numero = 4

numero_impar =5

[3] - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com dusa linhas em branco;
- métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - imports

- Imports devem  ser sempre feitos em linhas separadas;

# import Errado

import sys, os

# import Certo

import sys
import os

# Não há problemas em utilizar:

from types import String, ListType

# Caso tehna muitos imports de un mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutType,
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaiquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

funcao ( algo[ 1 ], { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# faça:

algo(1)

# Não faça:

dict ['chave'] = lista [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x               = 1
y               = 3
varialvel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova lihna
"""
