provas = {
    1:['a','b','c','d','e','f','g','h','i','j'],
    2:['a','b','c','e','d','a','b','c','e','d'],
    3:['f','g','h','i','j','f','g','h','i','j']
}
acertos = {
    1:0,
    2:0,
    3:0
}
aprovacao = 0
gabarito = ['a','b','c','d','e','f','g','h','i','j']
for matricula in provas:
    for questao in range(10):
        if provas[matricula][questao] == gabarito[questao]:
            acertos[matricula] +=1
    if acertos[matricula]>=7:
        aprovacao+=1
aprovacao = 100*aprovacao/len(provas)
[print(f'O aluno de matricula {i} teve {acertos[i]} acertos e seu gabarito foi:{provas[i]}') for i in provas]
print(f'O percentual de aprovação foi {aprovacao:.2f}')