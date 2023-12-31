n = []
for i in range(8):
    n.append(int(input(f'Digite o {i+1} número: ')))
x = int(input('Digite um valor positivo menor que 8: '))
y = int(input('Digite um valor positivo menor que 8: '))
print((n[x]+n[y]))