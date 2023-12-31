a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = 0
for i in range(len(a)):
    c += a[i]*b[i]
print(f'O produto escalar é {c}')