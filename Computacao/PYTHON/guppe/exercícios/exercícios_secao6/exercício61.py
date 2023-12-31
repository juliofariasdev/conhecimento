a = 100
b = 100
lista = []
while True:
    while True:
        print(a, b)
        algarismos = str(a*b)
        if algarismos == algarismos[::-1]:
            lista.append(a*b)
            break
        if a>998:
            break
        a += 1
    if a > 998 and b > 998:
        break
    a = 100
    b += 1
print(f'O maior palíndromo feito a partir do produto de dois números \nde dois digitos é {max(lista)}')