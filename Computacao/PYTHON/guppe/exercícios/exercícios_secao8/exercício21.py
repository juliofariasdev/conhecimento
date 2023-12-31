def primos_antes(n):
    """
    :param n: verifica a quantidade de números primos abaixo de n
    :return: retorna a quantidade de números primos abaixo de n
    """
    quantidade = 0
    contador = 0
    for i in range(1,n):
        contador = 0
        for c in range(1,i+1):
            if i%c==0:
                contador += 1
        if contador==2:
            quantidade+=1
    return quantidade
print(primos_antes(10000))
