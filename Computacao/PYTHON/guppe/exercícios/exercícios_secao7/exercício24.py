aluno = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
altura = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.8, 2]
print(f'O maior aluno é o {aluno[altura.index(max(altura))]}')
print(f'O menor aluno é o {aluno[altura.index(min(altura))]}')
"""relação = {}
for i in range(10):
    relação.update({input('Qual o código do aluno: '):(float(input('Qual a altura do aluno: ')))})
print(f'O menor aluno de número {relação.keys(min(relação.values()))}{min(relação.values())}')"""