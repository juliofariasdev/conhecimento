soma = 0
c= 1
while c <11:
    soma += float(input(f'Digite o {c}º número: '))
    c+=1
print(f'A média desses números é {soma/10:.1f}')