distancia = int(input('Distância percorrida, em Km: '))
litros_consumidos = int(input('Litros de gasolina consumidos: '))
consumo = distancia/litros_consumidos
if consumo<8:
    print(f'Venda seu carro!')
elif consumo>=8 and consumo<=12:
    print(f'Econômino!')
elif consumo>12:
    print(f'Super econômico!')