n = int(input('Digite um número interio positivo: '))
s1 = 0
s2 = 0
s3 = 0
for i in range(1,n+1):
    s1 +=i
    s2 +=i*(-1)**(i-1)
    s3 += 2*i -1
print(s1)
print(s2)
print(s3)