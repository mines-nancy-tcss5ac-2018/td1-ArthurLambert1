import os
os.chdir("C:/Users/Upriz/OneDrive/Bureau/MINES/INFO/TD 1")

def valeurLettre(x): #Fonction qui attribue à chaque lettre une valeur et la valeur 0 à '"'
    alphabet = ['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    taille = len(alphabet)
    for i in range(taille):
        if x == alphabet[i]:
            return(i)
    
def valeurMot(x): #Fonction qui donne la valeur d'un mot grace a la fonction precedente
    taille = len(x)
    valeur = 0
    for i in range(taille):
        valeur += valeurLettre(x[i])
    return valeur

def solve22():
    f = open("p022_names.txt", "r")
    liste = []
    for ligne in f:
        liste += ligne.split('","')
    liste[0] = 'MARY' #On modifie les premier et dernier termes qui sont pollués par des '"'
    liste[-1] = 'ALONSO'
    liste.sort()
    tailleFichier = len(liste)
    somme = 0
    for i in range(tailleFichier):
        somme += valeurMot(liste[i]) * (i+1)
    return somme


assert solve22() == 871198282
print(solve22())

'''nom.prenom@depinfonancy.net'''


    