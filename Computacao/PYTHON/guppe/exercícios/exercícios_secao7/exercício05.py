n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v = 0
for i in range(10):
    if n[i]%2==0:
        v += 1
print(f'A lista "n" tem {v} valores pares')