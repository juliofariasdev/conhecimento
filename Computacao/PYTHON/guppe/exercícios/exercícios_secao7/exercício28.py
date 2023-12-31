v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
v1 = []
v2 = []
for i in range(len(v)):
    if v[i]%2==0:
        v1.append(v[i])
    else:
        v2.append(v[i])
print(v1)
print(v2)