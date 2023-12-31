from math import radians, factorial

def sen(angulo):
    angulo = radians(angulo)
    return sum([(((-1)**n)*angulo**(2*n +1))/factorial(2*n+1) for n in range(6)])


print(sen(30))
