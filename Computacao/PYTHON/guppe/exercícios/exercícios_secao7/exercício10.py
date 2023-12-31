notas = []
for i in range(1,16):
    notas.append(int(input(f'Digite a nota do {i}º aluno: ')))
print(f'A média dessa turma é {sum(notas)/len(notas):.2f}')