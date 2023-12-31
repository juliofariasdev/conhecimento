lista = list(range(99,0,-1))
matriz = [[lista.pop() for j in range(5)] for i in range(5)]
[print(c) for c in matriz]