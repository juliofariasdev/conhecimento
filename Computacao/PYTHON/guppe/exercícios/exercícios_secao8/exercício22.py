def n_linhas(n):
    """
    n_linhas(n)
    :param n: quantidade a serem geradas
    :return: n linhas
    """
    def linhas():
        for i in range(1,n+1):
            print('!'*i)
        return 'FIM'
    return linhas()
print(n_linhas(10))