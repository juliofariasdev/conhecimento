matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
q =0
for i in matriz:
    for j in i:
        if j>10:
            print(j, end=' ')
            q +=1
print()
print(q)