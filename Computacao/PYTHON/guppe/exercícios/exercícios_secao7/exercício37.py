v = list(range(1, 12))
v.sort()
d = [v.pop(5) for i in range(5)]
d.reverse()
v.extend(d)
print(v)