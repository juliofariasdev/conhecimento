"""
Ententendo o **kwargs

Por conveção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extra
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetro extras em um dicionário.

#OBS: Os parâmetros *args e **kwargs não são obrigatótios.

ORDEM correta dos parâmetros:

def funcao(parametros_obrigatorios, *args, parametros_default, **kwargs):
    acao

**kwargs Desempacotar um dicionário.

OBS: Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função

"""