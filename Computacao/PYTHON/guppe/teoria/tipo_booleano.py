"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Falso
OBS: Sempre com inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operações básicas:
"""

# Negação (not):
"""
Fazendo negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o resultado será verdadeiro. ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# OU (or):

"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(logado or ativo)

# E (and):
"""
Também é uma operação binária. ou seja, depende de dois valores. Ambos os valores devem ser verdaderio.

True and True -> True 
True and False -> False 
False and True -> False 
False and False -> False
"""