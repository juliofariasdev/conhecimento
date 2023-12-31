n1 = 2*float(input('Qual a nota do trabalho do laboratório: '))
n2 = 3*float(input('Qual a nota da avalição semestral: '))
n3 = 5*float(input('Qual a nota do exame final: '))
media = (n1+n2+n3)/10
print(f'A média do aluno foi {media}')
if media<3:
    print(f'Aluno reprovado')
elif media>=3 and media<5:
    print(f'Aluno de recuperção')
elif media>=5:
    print(f'Aluno aprovado')
    