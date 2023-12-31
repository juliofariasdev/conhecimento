"""
Recebendo dados do usuário
"""
# Entrada de dados
# print("Qual o seu nome? ")
# nome = input() # input -> Entrada

nome = input("Qual o seu nome? ")

# Exemplo do print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" %nome)

# Exemplo do print 'moderno' 3.x
# print("Seja bem-vindo(a) {0}".format(nome))

# Exemplo do print "atual" 3.7
print(f"Seja bem-vindo(a) {nome}")

# print("Qual sua idade? ")
# idade = input()

idade = input("Qual sua idade? ")

# Processamento

# Saida
# Exemplo do print 'antigo' 2.x
# print("O %s tem %s anos"%(nome,idade))

# Exemplo do print 'moderno' 3.x
# print("O {0} tem {1} anos".format(nome,idade))

# Exemplo do print "atual" 3.7
print(f"O {nome} tem {idade} anos")

print(f"O {nome} nasceu em {2023 - int(idade)}")