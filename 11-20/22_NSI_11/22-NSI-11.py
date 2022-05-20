def recherche(tab,nb):
    for i in range(len(tab)):
        if tab[i] == nb: 
            return i 
    return -1

print(recherche([], 55) )

#ex2

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

"""
def cesar(message, decalage):
    resultat = ''
    for ... in message :
        if lettre in ALPHABET :
            indice = ( ... )%26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = ...
    return resultat
"""