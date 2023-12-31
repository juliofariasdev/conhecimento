def intercalador(palavra1, palavra2):
    nova_palavra = ''
    for i in range(min(len(palavra1),len(palavra2))):
        nova_palavra += palavra1[i]+palavra2[i]
    if palavra1[i+1] in palavra1:
        nova_palavra += palavra1[i+1]
    return nova_palavra


str2 = 'viera'
str1 = 'farias'

print(intercalador(str1, str2))