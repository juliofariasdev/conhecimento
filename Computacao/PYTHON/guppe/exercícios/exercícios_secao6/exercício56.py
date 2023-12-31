lista =[]
n = 1
while True:
    if n>=2000000:
        break
    i =None
    for i in range(2,n+1):
        if n%i==0:
            break
    if i ==n:
        print(n)
        lista.append(n)
    n +=1
print(f'A soma de todos os números \nprimos abaixo de dois milhões é {sum(lista)}')