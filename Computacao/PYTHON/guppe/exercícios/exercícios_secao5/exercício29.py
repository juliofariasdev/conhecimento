import random
acerto = 0
for i in range(5):
    a = random.randint(1,99)
    b = random.randint(1,99)
    resposta = int(input(f'Qual é soma {a} + {b} ? '))
    if resposta==(a+b):
        acerto +=1
print(f'O aluno acertou {acerto} vezes')