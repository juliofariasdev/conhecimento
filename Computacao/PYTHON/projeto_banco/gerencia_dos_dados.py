from main import login

with open('dados.txt') as arquivo:
    lines = arquivo.readlines()

def gerenciador(linhas):
    perfis = {}
    for linha in linhas:
        dados = linha.split(';')
        if '\n' in dados[3]:
            dados[3] = dados[3][:-1]
        perfis[dados[0]] = {
            'tipo': dados[1],
            'senha': dados[2],
            'valor': float(dados[3])
        }
    return perfis


def validador_de_login(usuario_passado,senha_passada):
    if usuario_passado in perfis_validos:
        if senha_passada == perfis_validos[usuario_passado]['senha']:
            return True
        else:
            return False


def transferencia(usuario_enviador,usuario_recebedor,quantia):
    perfis_validos[usuario_enviador]['valor'] -= quantia
    perfis_validos[usuario_recebedor]['valor'] += quantia


def sacar(usuario_sacador,saque):
    perfis_validos[usuario_sacador]['valor'] -= saque

perfis_validos = gerenciador(lines)
'''
perfis_validos = gerenciador(lines)
print(perfis_validos)
sacar('joao', 1000)
print(perfis_validos)'''
validador_de_login(login())