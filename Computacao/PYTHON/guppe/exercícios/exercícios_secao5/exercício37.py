print(f'Hora da chegada')

tempo_corrido=0
hora_inicial = int(input('hora: '))
minutos_inicial = int(input('minutos: '))

segundos_inicias = hora_inicial*3600 + minutos_inicial*60

print(f'''Tarifas
* 1º e 2º hora - R$1,00 cada
* 3º e 4º hora - R$1,40 cada
* 5º hora e seguintes - R$2,00 cada
''')
print(f'Hora de Partida')

hora_final = int(input('hora: '))
minutos_final = int(input('minutos: '))

segundos_finais =hora_final*3600 + minutos_final*60
if hora_final>=hora_inicial and minutos_final>=minutos_inicial:
    tempo_corrido= segundos_finais-segundos_inicias
elif hora_final<=hora_inicial and minutos_final<minutos_inicial:
    tempo_corrido= 24*3600-segundos_inicias + segundos_finais

if tempo_corrido%3600!=0:
    hora_percorrida = tempo_corrido//3600 +1
else:
    hora_percorrida = tempo_corrido//3600

if hora_percorrida<3:
    valor = hora_percorrida*1
elif hora_percorrida>=3 and hora_percorrida<5:
    valor = (hora_percorrida-2)*1.4+2
elif hora_percorrida>=5:
    valor = (hora_percorrida-4)*2+4.8

print(f'O valor final é R${valor}')