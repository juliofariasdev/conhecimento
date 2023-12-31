from collections import Counter

def anagrama(nome1,nome2):
    if Counter(nome1) == Counter(nome2):
        return True
    return False


print(anagrama('naa','ann'))