n_de_habitantes = int(input('Qual o número de habitantes de cavocalandia: '))
c1 = 0
c2 = 0
c3 = 0
min = 0
max = 0
for i in range(1, n_de_habitantes+1):
    kwh = int(input(f'Qual o consumo de kWh do {i}º habitante:'))
    categoria = str(input('''Qual a categoria do do habitante:    
    [1] - Residencial
    [2] - Comercial
    [3] - Industrial
    :'''))
    if categoria == '1':
        if i == 1:
            min = kwh
            max = kwh
        if kwh>max:
            max =kwh
        if kwh<min:
            min=kwh
        c1 += kwh
    elif categoria == '2':
        if i == 1:
            min = kwh
            max = kwh
        if kwh>max:
            max =kwh
        if kwh<min:
            min=kwh
        c2 += kwh
    elif categoria == '3':
        if i == 1:
            min = kwh
            max = kwh
        if kwh>max:
            max =kwh
        if kwh<min:
            min=kwh
        c3 += kwh
    else:
        print('categoria inválida')
print(f"O menor consumo foi {min}")
print(f'O maior consumo foi {max}')
print(f'A média do consumo foi {(c1+c2+c3)/n_de_habitantes:.2f}')
print(f'O consumo da categoria Residencial foi {c1}')
print(f'O consumo da categoria Comercial foi {c2}')
print(f'O consumo da categoria Industrial foi {c3}')
print('FIM DO PRAGRAMA')