a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
lista =[]
n = a+1
while True:
    if n==b:
        break
    i =None
    for i in range(2,n+1):
        if n%i==0:
            break
    if i ==n:
        lista.append(n)
    n +=1
print(f'A dos números primos entre {a} e {b} é {sum(lista)}')