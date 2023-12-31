from math import factorial

def superfatorial(n):
    sf = 1
    for i in range(n+1):
        sf *= factorial(i)
    return sf


print(superfatorial(3))