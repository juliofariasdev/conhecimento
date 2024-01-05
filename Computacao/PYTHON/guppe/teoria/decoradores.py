"""
Decoradores - Decoretors

def funcao_decoradora(funcao):
    def decorador():
        print('seja bem-vindo')
        funcao()
        print('estou aprendendo decorator ')
    return decorador

@funcao_decoradora -> decoretor
def nome():
    print('julio cesar da silva farias')


nome()

isso é mesmo que

def funcao_decoradora(funcao):
    def decorador():
        print('seja bem-vindo')
        funcao()
        print('estou aprendendo decorator')
    return decorador


def nome():
    print('julio cesar da silva farias')


nome = funcao_decoradora(nome)

nome()
"""

