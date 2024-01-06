"""
Preservando meta dados com wraps

Metadado  -> São dados intrísecos em arquivos

Wraos -> São funções que envolvem elementos com diversas finalidades.

def funcao_decoradora(funcao):
    @wraps(funcao)
    def decorador():
        acao
        funcao
    return decorador


@funcoa_decoradora
def funcao(param):
    acao
    return
"""