def sub_string(nome):
    for sub in nome:
        if len(sub)>1:
            return sub[0]
    return -1


print(sub_string(['c','d','silva','farias']))