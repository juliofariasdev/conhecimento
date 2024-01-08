notas = []
alunos = []
while True:
    nome = input('Qual a nome do aluno:')
    if nome == '0':
        break
    nota = input(f'Qual a noto da aluno {nome}: ')
    notas.append(nota)
    alunos.append(nome)

if len(notas) =='0':
    exit(1)
with open('exe20.txt', 'a') as file:
    for i in range(len(notas)):
        file.write(f'{alunos[i]}:{notas[i]}\n')