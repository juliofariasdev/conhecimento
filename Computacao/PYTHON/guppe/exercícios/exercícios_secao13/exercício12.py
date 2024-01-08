with open('exe12.txt') as file:
    text = file.read()
    words = text.split()
    file.seek(0)
    lines = file.readlines()

    lines_numbers = len(lines)
    words_numbers = len(words)
    chars_numbers = len(text)

    print(f'O arquivo contém {lines_numbers} linha(s)')
    print(f'O arquivo contém {words_numbers} palavra(s)')
    print(f'O arquivo contém {chars_numbers} caracter(s)')

    chars = text.upper()
    alfa = 'abcdefghijklmnopwrstuvwxyz'.upper()
    for char in alfa:
        quantidade = chars.count(char)
        print(f'A letra {char} aparece {quantidade} vezes no arquivo')