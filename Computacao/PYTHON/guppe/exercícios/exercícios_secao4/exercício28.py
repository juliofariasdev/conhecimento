from math import pow
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
soma_dos_quadrados = pow(n1, 2) + pow(n2, 2) + pow(n3, 2)
print(f'A soma dos quadrados desses três números vale {soma_dos_quadrados}')