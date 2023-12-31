n = [1,2,3,4,5]
while True:
    c = int(input('Digite o código: '))
    if c==0:
        print(f'FIM DO PROGRAMA')
        break
    elif c==1:
        for i in range(len(n)):
            print(n[i], end=' ')
        break
    elif c==2:
        n.reverse()
        for i in range(len(n)):
            print(n[i], end=' ')
        break
    else:
        print('Código inválido')