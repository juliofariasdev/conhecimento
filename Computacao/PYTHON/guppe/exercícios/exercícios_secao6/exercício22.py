lista =[]
while True:
    nota = int(input('Digite a uma nota: '))
    if nota not in range(10,21):
        print(f'{nota} é uma nota inválida')
        break
    lista.append(nota)
print(f'A média aritmética das notas válidas é {sum(lista)/len(lista):.2f}')
