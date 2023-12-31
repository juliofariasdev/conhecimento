def eh_um_triangulo(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 'Os lados do triângulo tem que ser positivo!'
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            return "É possivel formar um triângulo equilátero"
        elif a==b or a==c or c==b:
            return "É possivel formar um triângulo isósceles"
        return 'É possivel formar um triângulo escaleno'
    return 'Não é possivel formar um triângulo'
print(eh_um_triangulo(4,4,4))