"""
Decoradores com parâmetros

def funcaodecoradora_com_assinatura(valor):
    def interna(funcao):
        def decoretor(*args,**kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! O primeiro argumento precisa ser {valor}'
            return funcao(*args,**kwargs)
        return decoretor
    return interna


@funcaodecoradora_com_assinatura('html')
def linguagens(*args,**kwargs):
    return f'linguagens que eu conheço {", ".join(list(args))}'


print(linguagens('python', 'css'))
"""
