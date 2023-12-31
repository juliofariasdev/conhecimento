print("horário: ")
horas = int(input('horas: '))*3600
minutos = int(input('minutos: '))*60
segundos = int(input('segundos: '))
duracao = int(input('Duração, em segundos: '))
total = horas+minutos+segundos+duracao
print(f'A experiência biológica terminará no horário \n{total//3600} horas, {(total%3600)//60} minutos e {(total%3600)%60} segundos')