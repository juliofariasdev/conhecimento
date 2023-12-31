nota = float(input("Qual a nota do aluno: "))
n_de_faltas = int(input('Qual o número de falta do aluno: '))
print(f'O conceito do aluno é', end=' ')
if n_de_faltas<=20:
    if nota>=9:
        print('A')
    elif nota<9 and nota>=7.5:
        print('B')
    elif nota<7.5 and nota>=5:
        print('C')
    elif nota<5 and nota>=4:
        print('D')
    elif nota<4 and nota>=0:
        print('E')
if n_de_faltas>20:
    if nota>=9:
        print('B')
    elif nota<9 and nota>=7.5:
        print('C')
    elif nota<7.5 and nota>= 5:
        print('D')
    elif nota<5 and nota>=4:
        print('E')
    elif nota<4 and nota>=0:
        print('E')