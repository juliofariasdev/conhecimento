def media(a,b,c,escolha):
    if escolha=='A':
        return (a+b+c)/3
    elif escolha=='P':
        return (a*5 + b*3 + c*2)/10
print(media(6,10,15,'P'))