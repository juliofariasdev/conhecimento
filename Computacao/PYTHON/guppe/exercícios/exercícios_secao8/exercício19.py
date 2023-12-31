def maior_fator_primo(n):
    fator = None
    for i in range(2,n):
        v = 0
        if n%i==0:
            for c in range(2,i+1):
                if i%c==0:
                    v+=1
        if v==1:
            fator = i
    if fator==None:
        return n
    return fator
print(maior_fator_primo(11))