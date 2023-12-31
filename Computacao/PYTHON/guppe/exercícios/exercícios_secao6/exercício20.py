c = None
n_de_dados = 0
lista = []

while True:
    c = int(input("Digite um número inteiro: "))
    if c==1000:
        break
    n_de_dados +=1
    if c%2==0:
        lista.append(c)
print(f'Foram lidos {n_de_dados} e desses {len(lista)} pares')