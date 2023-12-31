n1 = int(input('Digite um número inteiro positivo: '))
n2 = int(input('Digite outro número inteiro positivo: '))
n3 = int(input('Digite mais um número inteiro positivo: '))
print(f'''Escolha uma opção:
[A] Média Geométrica
[B] Média Ponderada
[C] Média Harmônica
[D] Média Aritmética''')
opcao = str(input('Opção ')).upper()
if opcao=="A":
    print(f'A média Geométrica é {(n1*n2*n3)**(1/3):.2f}')
elif opcao=='B':
    print(f'A média Ponderada é {(n1+2*n2+3*n3)/6:.2f}')
elif opcao=='C':
    print(f'A média Hormônica é {1/((1/n1)+(1/n2)+(1/n3)):.2f}')
elif opcao=='D':
    print(f'A média Aritmética é {(n1+n2+n3)/3:.2f}')
else:
    print('Opção inválida!')