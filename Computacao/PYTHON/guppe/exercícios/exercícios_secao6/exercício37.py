n = 1000
v = 0
while n<=9999:
    if ((n%100) + (n//100))**2 == n :
        v +=1
    n +=1
print(f'{v}')