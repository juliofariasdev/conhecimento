n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = []
x = 2
for i in range(len(n)):
    if n[i]%x ==0:
        m.append(n[i])
print(f'Os múltiplos de {x} são: ',end='')
for i in range(len(m)):
    print(m[i], end=' ')