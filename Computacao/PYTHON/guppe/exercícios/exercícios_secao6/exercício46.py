from random import randint
n = randint(1, 1000)
t =0
while True:
    chute = int(input('Qual foi o número gerado: '))
    t +=1
    if chute == n:
        print(f'Você acertou com {t} tentativas')
        break
    elif chute>n:
        print(f'O chute é maior que o número gerado')
    else:
        print(f'O chute é menor que o número gerado')
    