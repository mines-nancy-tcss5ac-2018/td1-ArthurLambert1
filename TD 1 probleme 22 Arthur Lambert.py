def valeurLettre(x):
    alphabet = ['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    taille = len(alphabet)
    for i in range(taille):
        if x == alphabet[i]:
            return(i)
    



def solve22():
    f = open('p022_names.txt', 'r')
    liste = []
    for ligne in f:
        ligne.split()
        liste += ligne
    sorted(liste)
    tailleFichier = len(liste)
    somme = 0
    for i in range(tailleFichier):
        tailleMot = len(liste[i])
        sommePartielle = 0
        for j in range(tailleMot):
                sommePartielle = sommePartielle + valeurLettre(liste[i][j])
        somme = sommePartielle * (i+1)
    return somme

print(solve22())