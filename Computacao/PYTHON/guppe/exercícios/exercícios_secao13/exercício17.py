with open('exe17.txt') as file:
    A = file.readlines()
    A = [c.split() for c in A]
    posicoes = [(1,2),(1,0)]
    for p in posicoes:
        x = p[0]
        y = p[1]
        A[x][y] = 'r'
    for l in range(len(A)):
        for c in range(len(A)):
            if A[l][c] != 'r':
                A[l][c] = '1'
            else:
                A[l][c] = '0'

    A = [' '.join(c) for c in A]
with open('exe17-2.txt', 'w') as file:
    for linha in A:
        file.write(f'{linha}\n')