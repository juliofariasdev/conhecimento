soma = 0
v=0
for i in range(1,11):
    n = int(input(f'Digite o {i}º número inteiro positivo: '))
    if n>0:
        soma +=n
        v+=1
if v!=0:
    print(f'A média desses números é {soma/v:.2f}')
else:
    print(f'Nenhum número foi digitado!')