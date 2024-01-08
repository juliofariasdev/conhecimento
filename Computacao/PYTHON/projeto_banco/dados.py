class Usuarios:
    def __init__(self, nome, senha):
        self.name = nome
        self.senha = senha


class Contas:

    def __init__(self):
        pass

def abertura():
    # abertura -> lista dos usuários

    with open('usuarios.txt') as file:
        lines = file.readlines()
        lista_de_usuarios = []
        for usuario in lines:
            usuario = usuario.split(':')
            lista_de_usuarios.append(Usuarios(usuario[0], usuario[1] if usuario[1][-1] != '\n' else usuario[1][:-1]))
    return lista_de_usuarios


def atualizar(lista_atualiza):
    # atualiza os dados
    with open('usuarios.txt', 'w') as file:
        for usuario in lista_atualiza:
            usuario = usuario.__dict__
            file.write(f'{usuario["name"]}:{usuario["senha"]}\n')


def adicionar(novo_usuario):
    # adiciona uma nova conta
    with open('usuarios.txt', 'a') as file:
        novo_usuario = novo_usuario.__dict__
        file.write(f'{novo_usuario["name"]}:{novo_usuario["senha"]}\n')


def criar_conta(nome_cadastrada,senha_cadastrada):
    # Adiciona um novo usuário
    usuario_novo = Usuarios(nome_cadastrada,senha_cadastrada,)
    adicionar(usuario_novo)


def remover_conta(conta):
    # Remove uma conta
    contas.remove(conta)
    atualizar(contas)

"""
contas = abertura()
print(contas)
print(contas)
for i in abertura():
    print(i.__dict__)
"""
