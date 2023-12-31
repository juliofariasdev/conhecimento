from math import radians, factorial

def senh(angulo):
    angulo = radians(angulo)
    return sum([(angulo**(2*n +1))/factorial(2*n+1) for n in range(6)])


print(senh(10))