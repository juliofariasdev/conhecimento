def data_atual(data):
    mes = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro' , 11: 'novembro', 12: 'dezembro'}
    extenso = str(data).lstrip('0').split("/")
    print(f'{extenso[0]} de {mes[int(extenso[1].strip("0"))]} de {extenso[2]}')
data_atual('10/4/2000')
