respostas = [
    ['a','b','c','e','d','a','b','c','e','d'],
    ['b','c','d','a','e','b','c','d','a','e'],
    ['e','d','c','b','a','d','b','a','c','e'],
    ['d','b','a','c','e','a','b','c','d','e'],
    ['a','b','c','d','e','e','d','c','b','a']
]
gabarito = ['a','b','c','d','e','e','d','c','b','a']
for i in range(5):
    acertos = 0
    for j in range(10):
        if respostas[i][j]==gabarito[j]:
            acertos +=1
    print(f'O {i+1}º aluno acertou {acertos} questões')