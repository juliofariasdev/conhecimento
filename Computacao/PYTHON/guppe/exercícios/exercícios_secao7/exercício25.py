a = []
c = 1
while len(a)<=100:
    if c%7!=0 or str(c).split()[len(str(c).split())-1] !="7":
        a.append(c)
    c +=1
print(a)