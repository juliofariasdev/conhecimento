from math import fabs

def triangulo_lateral(n):
    """
    gera um triângulo lateral de altura 2*n-1 e n largura.
    :param n: largura do triângulo
    :return: rertona o triângulo lateral
    """
    for i in range(1,1+n):
        print('*'*i)
    for i in range(n-1,1,-1):
        print('*'*i)
    return '*'
print(triangulo_lateral(9))