from random import randint

n = 5
for i in range(n):
    d1 = randint(1,6)
    d2 = randint(1,6)
    if d1> d2:
        print(f'O número do primeiro dado foi {d1} e maior que \no número do segundo dado que foi {d2}.')
    elif d1< d2:
        print(f'O número do segundo dado foi {d2} e maior que \no número do primeiro dado que foi {d1}.')
    else:
        print(f'O númeos do dados foram iguais a {d2}.')
