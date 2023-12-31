def fatorial(n):
    nf = 1
    if n < 0:
        return None
    while n > 0:
        nf *= n
        n -= 1
    return nf
print(fatorial(4))