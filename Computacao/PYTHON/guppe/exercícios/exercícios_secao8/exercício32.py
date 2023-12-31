def simplifica(numerador, denominador):
    i = 1
    while i <= denominador:
        i +=1
        if numerador%i==0 and denominador%i==0:
            numerador /=i
            denominador /=i
            i -= 1
    return f'{numerador:.0f}/{denominador:.0f}'


print(simplifica(72,120))