def operacao(a,b,simbolo):
    if simbolo == '+':
        return a+b
    elif simbolo == '-':
        return a-b
    elif simbolo == '*':
        return a*b
    elif simbolo == '/':
        return a/b
print(operacao(9,3,'/'))