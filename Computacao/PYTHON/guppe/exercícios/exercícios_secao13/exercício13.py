with open('exe13.txt', 'a') as file:
    while True:
        number = input('Digite um número de telefone, somente números: ')
        if number =="0":
            break
        nome = input('Digite o nome do dono número do telefone: ')
        file.write(f'{nome} - {number}\n')
