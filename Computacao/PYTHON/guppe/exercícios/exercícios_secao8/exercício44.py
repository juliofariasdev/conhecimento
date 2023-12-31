def parimpar(lista):
    a = []
    b = []

    for i in lista:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    return a,b


print(parimpar(list(range(10))))