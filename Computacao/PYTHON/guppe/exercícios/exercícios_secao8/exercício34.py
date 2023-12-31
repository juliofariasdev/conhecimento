def duplo_fatorial(n):
    df =1
    for i in range(1,n+1,2):
        df *=i
    return df


print(duplo_fatorial(6))