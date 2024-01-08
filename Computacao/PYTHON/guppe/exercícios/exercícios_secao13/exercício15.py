with open('exe14-2.txt') as file:
    lines = file.readlines()
    idades = [int(line.split()[1]) for line in lines]
with open('exe15.txt', 'w') as file:
    i = 0
    for line in lines:
        if idades[i]>18:
            text = 'maior de idade'
        elif idades[i]<18:
            text = 'menor de idade'
        else:
            text = 'entrado para maior idade'
        file.write(f'{line.split()[0]} {text}\n')
        i+=1