"""
Tipo string

Em python, um dado é considerado tipo string sempre que:

-Estiver entre áspas simples -> 'uma string', '234', 'a', 'True', '42.3'
-Estiver entre áspas duplas -> "uma string", "234", "a", "True", "42.3"
-Estiver entre áspas simples tiplas -> '''uma string''', '''234''', '''a''', '''True'''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:4]) # Slice de string

print(nome[5:15])

print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre áspas duplas tiplas

nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1]) # Inversão de String Pythônico

print(nome.replace('e', 'i'))
