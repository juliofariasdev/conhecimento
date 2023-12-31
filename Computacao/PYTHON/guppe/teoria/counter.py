"""
Módulo Collections - Counter (Contador)

Collections -> High-performace Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências
desse elemento.

from Collections import Counter

Counter(interável) -> devolve {valor do interável: número de ocorrências do valor}

Counter(interável).most_common(quantidade) -> delvove os valores com mais ocorrência de acordo com a quantidade
"""
from collections import Counter
d = {'j': 5, 'u': 2, 'l': 3}
print(Counter(d).most_common())