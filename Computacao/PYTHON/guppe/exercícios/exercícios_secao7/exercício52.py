lista = list(range(16,0, -1))
matriz = [[lista.pop() if i>=j else 0 for j in range(4)]for i in range(4)]
print(matriz)