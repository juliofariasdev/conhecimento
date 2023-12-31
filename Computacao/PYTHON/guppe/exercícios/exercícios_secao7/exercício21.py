A = set({})
B = set({})
for i in range(10):
    A.add(int(input('Digite um valor do conjunto A: ')))
for i in range(10):
    B.add(int(input('Digite um valor do conjunto B: ')))
C = A.difference(B)
print(f'A diferença entre o conjunto A e o conjunto B é {C}')
