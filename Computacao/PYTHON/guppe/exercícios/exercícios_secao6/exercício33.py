n = 10
i = 11
j = 17
d= 0
lista= []
while len(lista) < n:
    if d%i == 0 or d%j ==0:
        lista.append(d)
    d+=1
print(f'os {n} primeiros múltiplos de {i} ou {j} são {lista}')