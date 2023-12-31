from math import radians, factorial

def cosh(angulo):
    angulo = radians(angulo)
    return sum([(angulo**(2*n))/factorial(2*n) for n in range(6)])


print(cosh(90))