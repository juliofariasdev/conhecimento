from math import radians, factorial

def cos(angulo):
    """

    :param angulo:
    :return:
    """
    angulo = radians(angulo)
    return sum([(((-1)**n)*angulo**(2*n))/factorial(2*n) for n in range(6)])


print(cos(60))