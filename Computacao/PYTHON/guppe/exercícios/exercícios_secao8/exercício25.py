def soma(n):
    s = 0
    for i in range(1,n+1):
        s += (n**2 +1)/(n+3)
    return s
print(soma(1000000))