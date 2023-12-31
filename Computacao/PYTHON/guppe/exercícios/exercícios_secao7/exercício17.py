n = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
for i in range(len(n)):
    if n[i]< 0:
        n[i] =0
for i in range(len(n)):
    print(n[i], end=' ')