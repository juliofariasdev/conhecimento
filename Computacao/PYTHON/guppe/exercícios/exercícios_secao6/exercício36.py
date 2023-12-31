soma1 = []
soma2 = []
for i in range(1,101):
    soma1.append(i**2)
    soma2.append(i)
soma1 = sum(soma1)
soma2 = sum(soma2)**2
print(f'A diferença entre a soma dos quadrados dos cem \nprimeros números naturais e \no quadrado da soma é {soma2-soma1}')
