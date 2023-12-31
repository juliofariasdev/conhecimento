n1 = float(input('Qual foi a nota da primeira prova: '))
n2 = float(input('Qual foi a nota da segunda prova: '))
n3 = 2*float(input('Qual foi a nota da terceira prova: '))
media_ponderada = (n1+n2+n3)/4
print(f'A média do aluno foi {media_ponderada}')
if media_ponderada>= 6:
    print(f'O aluno foi aprovado')
else:
    print(f'O aluno foi reprovado')