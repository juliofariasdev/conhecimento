from random import randint

a = randint(0, 1000)
b = randint(0, 1000)
v1 = [i for i in str(a)[::-1]]
v2 = [c for c in str(b)[::-1]]
v3 = [a+b]
print(v1, v2, v3)