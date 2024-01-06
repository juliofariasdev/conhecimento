"""
POO - Atributos

Atributos são características do objeto da classe

Em Python os atributos são dividos em 3:

class Classe:
    # Isso é um atributo classe, Ele é atributo a qualquer instância da classe.
    atributo_de_classe = algo

    # __init__ -> método que cria um objeto, sendo um método uma função dentro de uma classe.
    def __init__(self,atributo, senha):
        # Isso é um atributo de instância, Ele é atributo apenas ao próprio objeto.
        self.atributo_de_instancia = atributo

        # Isso é um atributo privado, Ele é declarado com "__atributo".
        self.__senha = senha

    # Isso é um método.
    def mostrar_atributo(self):
        print(self.atributo)

objeto = Classe('julio', 123)

objeto.atributo_de_instancia -> Acessa o atributo de instância

Classe.atributo_de_classe -> Acessa o atributo de classe

objeto.atributo_dinamica = 'hoje' -> Cria um atributo dinâmico.

objeto._Classe__senha -> Acessa o atributo privado

del objeto.atributo_dinamica -> Deletar um atributo.

"""