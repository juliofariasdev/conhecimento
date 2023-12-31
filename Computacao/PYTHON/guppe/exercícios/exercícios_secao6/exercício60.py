lista =[]
listapar = []
while True:
    n = int(input('Digite qualquer número: '))
    if n ==0:
        break
    lista.append(n)
    if n%2==0:
        listapar.append(n)
print(f'A soma dos números digitados é {sum(lista)}')
print(f'A quantidade de números digitados foi {len(lista)}')
print(f'A média dos números digitados é {sum(lista)/len(lista):.2f}')
print(f'O maior número digitado foi {max(lista)}')
print(f'O menor número digitado foi {min(lista)}')
print(f'A média dos números pares é {sum(listapar)/len(listapar):.2f}')