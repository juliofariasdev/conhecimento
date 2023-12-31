def economia(distancia,litros):
    consumo = distancia/litros
    if consumo<8:
        return 'Venda seu carro!'
    elif consumo<14:
        return 'Econômico!'
    return 'Super econômico!'
print(economia(10,10))