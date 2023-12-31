n = []
soma_p = 0
quantidade_n = 0
for i in range(10):
    n.append(int(input('Digite um valor: ')))
for i in range(10):
    if n[i] > 0:
        soma_p+=n[i]
    elif n[i] < 0:
        quantidade_n +=1
print(f'Quantidade de números lidos negativos é {quantidade_n}')
print(f'A soma dos números positivos lidos é {soma_p}')