"""
Reduce

OBS: A partir do Puthon3+ a função reduce() não é mais uma função integrada (built-in). Agora temos
 que importar e utilizar esta função a partir do módulo 'functools'

 Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
 99% das vezes um loop for é mais legível.

 funcionamento:

 reduce(funcao, interavel) ->
    retorna funcao(a1,a2)
    retorna funcao(res1,a3)
    retorna funcao(res2,a4)
    ...
    retorna funcao(res(n-1),an)
"""