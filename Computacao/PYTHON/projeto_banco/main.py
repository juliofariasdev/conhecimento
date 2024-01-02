import time
def banco():

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

    def logi():
        usuario = input('Usuário: ').lower()
        senha = input('Senha: ')
        carregamento()
        return (usuario,senha)


    def tela_de_usuario(perfil):
        print(f'Bem-vindo {str()}')

    tela_de_usuario(perfis_validos)

# banco()


def login():
    usuario = input('Usuário: ').lower()
    senha = input('Senha: ')
    carregamento()
