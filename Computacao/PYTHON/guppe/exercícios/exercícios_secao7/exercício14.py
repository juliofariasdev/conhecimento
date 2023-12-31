n = [1, 1, 2, 2, 3, 4, 5, 6, 7, 8]
for i in range(len(n)):
    for k in range(i+1,len(n)):
        if n[i] == n[k]:
            print(f'O número {n[i]} se repete')