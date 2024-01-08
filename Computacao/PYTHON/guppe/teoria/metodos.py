"""
POO - Métodos

Métodos - Mundam o comportamento de uma instância, sendo uma função dentro de classe.

Os métodos são classificado em 3 categorias:
Métodos de instância
Métodos de classe
Métodos estáticos

Um método mágico é aquele que contém dunder - __init__

__metodo -> é criado um método privado

class Classe:

    atributo_de_classe = algo

    __init__(self, atributo):
        self.atributo = atributo

    # Cria um método de instância
    def metodo_de_instancia(self):
        acao com o atributo de instancia


    # Cria um método de classe usando um decorador classmethod
    @classmethod
    def metodo_de_classe(cls):
        acao com atributo de classe

    # Cria um método estático usando um decorador staticmethod
    @staticmethod
    def metodo_estatico():
        acao

    # Cria um método privado
    def __metodo_privado(self):
        acao

objeto = Classe(atributo)

# Acessa o método de instância
objeto.metodo_de_instancia

# Acessa o método de classe
Class.metodo_de_class

# Acessa o método estático
objeto.metodo_estatico or Classe.metodo_estatico

# Acessa o método privado
objeto._Classe__metodo_privado

"""