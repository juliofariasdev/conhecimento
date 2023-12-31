x = list(range(1,6))
y = list(range(6,11))
s = [(x[i] + y[i]) for i in range(5)]
p = [(x[i] * y[i]) for i in range(5)]
d = set(x).difference(set(y))
i = set(x).intersection(set(y))
u = set(x).union(set(y))
print(f'A soma x e y é : {str(s).strip("[" "]")}')
print(f'O produto entre x e y é : {str(p).strip("[" "]")}')
print(f'A diferença entre x e y é: {str(d).strip("{" "}")}')
print(f'A união entre x e y é : {str(u).strip("{" "}")}')
if i == set():
    print('Não existe interseção entre x e y')
else:
    print(f'A interseção entre x e y é: {str(i).strip("{" "}")}')