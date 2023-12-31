N = int(input('Digite um número inteiro: '))
lista =[]
n = 1
while True:
    if len(lista) == N:
        break
    i =None
    for i in range(2,n+1):
        if n%i==0:
            break
    if i ==n:
        lista.append(n)
    n +=1
print(f'A soma dos {N} primeiros números é {sum(lista)}')