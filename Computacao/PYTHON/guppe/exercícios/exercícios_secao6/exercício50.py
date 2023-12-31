h_de_chico = 1.5
h_de_ze = 1.1
v =1
while True:
    if(h_de_ze+0.03*v)> (h_de_chico+0.02*v):
        break
    v+=1
print(f'{v} serão necessários para que Zé seja maior que Chico')