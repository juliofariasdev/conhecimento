def produto(A,B):
    ordem = len(A)
    B = [[B[j][i] for j in range(ordem)] for i in range(ordem)]
    C = [[]for _ in range(ordem*2)]
    l =0
    k =0
    for i in range(ordem):
        l += i
        k=0
        for j in range(ordem):
            C[l].append(A[i][j]*B[k][j])
        l+=1
        k=+1
        for j in range(ordem):
            C[l].append(A[i][j]*B[k][j])
    return [sum(i) for i in C]



a = [
    [3, 4],
    [5, 1]
]
b = [
    [1,0],
    [0,1]
]

print(a)
print(b)
print(produto(a,b))