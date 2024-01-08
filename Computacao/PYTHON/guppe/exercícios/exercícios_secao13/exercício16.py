vetor = [bin(i)[2:] for i in range(10)]
with open('exe16.txt', 'w') as file:
    for dado in vetor:
        file.write(dado+'\n')