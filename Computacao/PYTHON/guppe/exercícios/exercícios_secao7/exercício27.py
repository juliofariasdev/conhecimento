v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(v)):
    k =0
    for c in range(1, max(v)+1):
        if v[i]%c==0:
            k += 1
    if k == 2:
        print(f'{v[i]} é primo e sua posição no vetor é {v.index(v[i])}')