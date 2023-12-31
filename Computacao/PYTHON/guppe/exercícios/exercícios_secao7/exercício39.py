from math import factorial


def termo(i,f):
    return f'{(factorial(i))/(factorial(f)*factorial(i-f)):.0f}'
n = 20
numeros_de_linhas = 0
for i in range(n):
        for f in range(numeros_de_linhas+1):
            print(termo(i,f), end=' ')
        print()
        numeros_de_linhas += 1



