with open('exe18.txt') as file:
    lines = file.readlines()
total =0
for line in lines:
    total += float(line.split()[-1])
print(f'O total da compra foi R${total}')