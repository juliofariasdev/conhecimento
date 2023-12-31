n = []
for i in range(5):
    n.append(int(input('Digite um valor: ')))
print(f'O maior valor que é {max(n)} se encontrar na posição {n.index(max(n))}')
print(f'O menor valor que é {min(n)} se encontrar na posição {n.index(min(n))}')