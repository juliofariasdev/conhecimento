v = [1, 2, 3, 4, 5, 6]
vpar = []
vimpar = []
for i in range(len(v)):
    if v[i]%2==0:
        vpar.append(v[i])
    else:
        vimpar.append(v[i])
print(f'Os números pares digitados foram: ', end='')
for i in range(len(vpar)):
    print(vpar[i], end=' ')
print()
print(f'A soma dos números pares digitados é : {sum(vpar)}')
print(f'Os números ímpares digitados foram: ', end='')
for i in range(len(vimpar)):
    print(vimpar[i], end=' ')
print()
print(f'A quantidade de números ímpares digitados é : {len(vimpar)}')
