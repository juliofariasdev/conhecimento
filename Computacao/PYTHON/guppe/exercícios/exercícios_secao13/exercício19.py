with open('exe19.txt') as file:
    lines = file.readlines()
notas ={}
for line in lines:
    notas[float(line.split(':')[-1])] = line.split(':')[0]
maior_nota = max(notas)
melhor_aluno = notas[maior_nota]
print(f'O melhor aluno foi {melhor_aluno} que possui a nota {maior_nota}')