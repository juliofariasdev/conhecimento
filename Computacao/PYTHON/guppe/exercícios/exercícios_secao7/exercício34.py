v =[]
while len(v)<=10:
    c = int(input('Digite um valor: '))
    if c not in v:
        v.append(c)
    else:
        print('Esse valor já foi digitado! tente outro valor')
print(v)