b = 1
lista = []
while True:
    a = 1
    while True:
        c = (a**2 + b**2)**0.5
        if (a+b+c) == 1000:
            lista.extend([a, b, int(c)])
            break
        if (a+b+c)>1000:
            break
        a +=1
    if len(lista) ==3:
        break
    b +=1
print(a,b,int(c))