import dados


def verificador_de_login(usuario_passado,senha_passada):
    # Verifica se as senhas passadas são validas
    logado = False
    for usurio_valido in dados.abertura():
        if usuario_passado == usurio_valido.name:
            if senha_passada == usurio_valido.senha:
                logado = True
                break
    return logado


