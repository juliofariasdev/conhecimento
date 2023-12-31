from random import randint
n = []
m = []
for i in range(10):
    n.append(randint(0, 50))
for i in range(len(n)):
    if n[i]%2!=0:
        m.append(n[i])
i =0
print(f'Lista 1: ')
while i in range(len(n)):
    c =0
    for c in range(2):
        print(n[i], end=' ')
        i +=1
    print()
print(f'Lista 2: ')
i = 0
while i in range(len(m)):
    c = 0
    for c in range(2):
        if i == len(m):
            break
        print(m[i], end=' ')
        i += 1
    print()