def nombreMiroir(x): #Retourne le nombre à l'envers
    chaine = str(x)
    chaineRenversee = ''
    for elt in chaine:
        chaineRenversee = elt + chaineRenversee
    return int(chaineRenversee)

def testPalindrome(x): #Teste si un nombre est palindrome ou non
    return x == nombreMiroir(x)
    
def testLychrel(n):
    for i in range(50):
        n += nombreMiroir(n)
        if testPalindrome(n):
            return 1
    return 0
    
def solve55(n): 
    l = list(range(10, n + 1))
    resultat = 0
    for x in l:
        if testLychrel(x) == 0:
            resultat += 1
    return resultat

assert solve55(10000) == 249
print(solve55(10000))
        