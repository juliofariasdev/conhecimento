import math

S = []
for i in range(1,6):
    S.append(i/math.factorial(2*i))
print(f'O Valor de S é {sum(S)}')