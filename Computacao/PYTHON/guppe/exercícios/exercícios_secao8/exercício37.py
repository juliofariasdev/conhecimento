def hiperfatorial(n):
    h = 1
    for i in range(1, n+1):
        h *= i**i
    return h


print(hiperfatorial(10))