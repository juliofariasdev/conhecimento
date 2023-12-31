idades = []
while True:
    idade = int(input('Qual a sua idade: '))
    if idade<=0:
        break
    idades.append(idade)
print(f'A média dessas idades é {sum(idades)/len(idades):.2f}')