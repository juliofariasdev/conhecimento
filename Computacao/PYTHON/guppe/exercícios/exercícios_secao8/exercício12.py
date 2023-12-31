def soma_algarismo(n):
    if n<=0:
        return 'Número inválido.'
    algarismos = [int(str(n)[i]) for i in range(len(str(n)))]
    return sum(algarismos)
print(soma_algarismo(2))