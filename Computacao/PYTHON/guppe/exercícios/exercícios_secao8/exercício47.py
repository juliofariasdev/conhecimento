def maiores10(matriz):
    contador =0
    for i in matriz:
        for j in i:
            if j > 10:
                contador += 1
    return contador


A = [[(i+1)**(j+1)for j in range(4)] for i in range(4)]
print(maiores10(A))