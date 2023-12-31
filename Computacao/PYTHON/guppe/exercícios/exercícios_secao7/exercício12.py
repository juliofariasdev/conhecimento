n = []
for i in range(5):
    n.append(int(input('Digite um valor: ')))
print(f'Os valores lidos foram ', end=': ')
for i in range(5):
    print(n[i], end=' ')
print()
print(f'O maior número lido foi {max(n)}')
print(f'O menor número lido foi {min(n)}')
print(f'A média dos valores lidos é {sum(n)/len(n):.2f}')
