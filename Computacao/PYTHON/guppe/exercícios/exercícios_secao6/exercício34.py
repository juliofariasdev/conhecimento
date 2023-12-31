n = 1
while True:
    d = 1
    for d in range(1,21):
        if n%d !=0:
            break
    if d ==20:
        break
    n +=1
print(f'{n} é primeiro número múltiplo de todos os números de 1 a 20')