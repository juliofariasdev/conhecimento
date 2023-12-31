total = 0
def unidade():
    total = 0
    for i in range(1,6):
        algarismos = str(i)
        if algarismos[len(algarismos)-1]  == '1':
            total += 2
        elif algarismos[len(algarismos)-1] in ('2', '3', '6', '7', '8', '9'):
            total += 4
        elif algarismos[len(algarismos)-1] in ('5'):
            total +=5
        elif algarismos[len(algarismos)-1] in ('4'):
            total +=6
    return total
print(unidade())