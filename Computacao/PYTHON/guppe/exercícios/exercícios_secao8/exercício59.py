def uniao(a,b):
    u = []
    for i in a:
        if i in b:
            u.append(i)
    return list(set(u))


print(uniao([1,2,3,4,5,4],[3,4,5,6,7,4]))