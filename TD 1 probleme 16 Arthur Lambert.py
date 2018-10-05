def solve16(n):
    a = str(2**n)
    taille = len(a)
    somme = 0
    for i in range(taille):
        somme += int(a[i])
    return somme

assert solve16(15) == 26
print(solve16(15))
    