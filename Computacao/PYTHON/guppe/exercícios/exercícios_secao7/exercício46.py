matriz = [[] for _ in range(10)]
for i in range(1,11):
    for j in range(1,11):
        if i<j:
            matriz[i-1].append(2*i +7*j -2)
        elif i==j:
            matriz[i-1].append(3*(i**2) -1)
        else:
            matriz[i-1].append(4*(i**3) -5*(j**2) +1)
print(matriz)