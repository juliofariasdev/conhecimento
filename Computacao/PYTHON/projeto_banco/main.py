import time

def organizador(dado):
    dado = str(dado).split(';')
    panilha = [
        {dado[1]: [dado[0],dado[2],dado[3]]}
    ]

def inicializa(User,password):
    pass


def carregamento():
    print('Carregando', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.', end='')
    time.sleep(0.5)
    print('.')


def titulo():
    print(20*'==')
    print(13*' '+'BANCO FARIAS')
    print(20 * '==')
    carregamento()

def login():
    usuario = input('Usuário: ').lower()
    senha = input('Senha: ')
    carregamento()
    return (usuario,senha)


with open('dados.txt') as arquivo:
    dados = arquivo.readlines()
    # infor = map(organizador(),dados)
#titulo()
#login()