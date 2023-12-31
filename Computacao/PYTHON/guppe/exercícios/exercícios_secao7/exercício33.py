l = list(range(14))
l.insert(6, 0)
l.insert(15, 0)
print(l)
for i, item in enumerate(l):
    if item ==0:
        l.pop(i)
print(l)