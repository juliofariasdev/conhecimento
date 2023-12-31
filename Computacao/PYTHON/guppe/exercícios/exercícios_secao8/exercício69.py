def mdc(fração):
    MDC = 1
    numerador = int(fração.split('/')[0])
    denominador = int(fração.split('/')[1])
    for i in range(1,min(numerador,denominador)+1):
        if not numerador%i and not denominador%i:
            MDC = i
    numerador_simplificado = numerador//MDC
    denominador_simplifiacado = denominador//MDC



def somador_de_fracoes():
    print()


p = '12/8'
q = '25/15'
print(MDC(q))