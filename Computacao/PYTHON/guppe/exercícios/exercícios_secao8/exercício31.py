from math import factorial

def neperiano(n):
    return sum([(1/factorial(i)) for i in range(n+1)])


print(neperiano(10000))