segmento1 = int(input('Primeiro comprimento: '))
segmento2 = int(input('Segundo comprimento: '))
segmento3 = int(input('Terceiro comprimento: '))
if (segmento3+segmento2)>segmento1 and (segmento3+segmento1)>segmento2 and (segmento2+segmento1)>segmento3:
    print('é possivel formar um tirângulo com esses comprimento')
    if segmento3==segmento1==segmento2:
        print('E é um triângulo equilátero')
    elif segmento3==segmento1 or segmento1==segmento2 or segmento3==segmento2:
        print('E é um triângulo isósceles')
    elif segmento3!=segmento2!=segmento1:
        print('E é um triângulo escaleno')
else:
    print('Não é possivel formar um triângulo com esses comprimento')
