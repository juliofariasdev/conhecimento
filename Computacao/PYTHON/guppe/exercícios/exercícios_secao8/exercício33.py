from math import factorial

def algarismos_de_n(n):
    return sum([int(i) for i in str(factorial(n))])


print(algarismos_de_n(5))