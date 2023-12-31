n = []
q = []
for i in range(1,11):
    n.append(int(input(f'Digite o {i}º número real: ')))
    q.append(n[i-1]**2)
for i in range(0, 10):
    print(f'{n[i]} ,{q[i]}', end='; ')