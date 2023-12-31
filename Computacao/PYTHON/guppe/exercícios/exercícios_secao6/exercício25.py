lista = []
for i in range(1,1000):
    if i % 3 ==0 or i % 5 == 0:
        lista.append(i)
print(f'{sum(lista)} é a soma dos números de três algarismos \nque são múltiplos de 3 ou 5')