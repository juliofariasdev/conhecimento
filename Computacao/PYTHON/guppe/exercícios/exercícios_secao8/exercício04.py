def quadrado_perfeito(n):
    if n>=0 and (n**0.5)%1==0:
        return f'{n} é um quadrado perfeito'
    else:
        return f'{n} não é um quadrodo perfeito'
print(quadrado_perfeito(9))