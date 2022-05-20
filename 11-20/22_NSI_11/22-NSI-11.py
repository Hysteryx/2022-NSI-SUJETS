def recherche(tab,nb):
    for i in range(len(tab)):
        if tab[i] == nb: 
            return i 
    return -1

#ex2

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''
    for lettre in message :
        if lettre in ALPHABET :
            indice = ( position_alphabet(lettre) + decalage )%26 #si la lettre est a décallée on lui prend sa position + le décallage 
            resultat = resultat + ALPHABET[indice] #on lui met l'ancien texte + la nvelle lettre 
        else:
            resultat = resultat + lettre #sinon on lui met la lettre normal 
    return resultat
