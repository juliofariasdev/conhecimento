t =1
while True:
    if (30*(1.046**t))<=(10*(1.05**t)):
        break
    t +=1
print(f'{t} são necessários para que o valor pertencente a João igule ou ultrapasse o valor pertencente a Carlos')