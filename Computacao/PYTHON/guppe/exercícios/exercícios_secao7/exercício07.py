n = []
for i in range(10):
    n.append(int(input('Digite um valor: ')))
print(f'O maior valor lido foi {max(n)} e se encontra na posição {n.index(max(n))}')