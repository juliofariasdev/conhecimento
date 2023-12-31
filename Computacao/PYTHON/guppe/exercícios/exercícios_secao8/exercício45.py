def desvio_padrao(lista):
    n = len(lista)
    m = sum(lista)/n
    soma =0
    for i in range(n):
        soma += (lista[i] -m)**2
    df = soma/(n-1)
    return df


print(desvio_padrao([1,2,3]))