import datetime

ano = datetime.date.today().year

with open('exe14.txt') as file:
    lines = file.readlines()
    anos_de_nascimento = [line.split()[1:] for line in lines]
anos_de_nascimento = [[int(i) for i in date] for date in anos_de_nascimento]
idades = []
for i in anos_de_nascimento:
    idades.append(ano - i[2])
c = 0
with open('exe14-2.txt', 'w') as file:
    for i in lines:
        file.write(f'{i.split()[0]} {idades[c]} anos \n')
        c +=1