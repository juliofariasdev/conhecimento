n = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9, 10, 10, 11, 11, 11, 12, 12]
q = 0
for i in range(len(n)):
    print(n[i], end=' ')
print()
for i in range(len(n)):
    if len(n)-1<i:
        break
    q = n.count(n[i])
    if q>1:
        for k in range(1,q):
            n.remove(n[i])
for i in range(len(n)):
    print(n[i], end=' ')