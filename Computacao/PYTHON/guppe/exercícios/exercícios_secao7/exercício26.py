v = list(range(10))
n = len(v)
m = sum(v)/n
soma = 0
for i in range(n):
    soma += (v[i]-m)**2
desvio_padrão = (soma/(n-1))**0.5
print(desvio_padrão)