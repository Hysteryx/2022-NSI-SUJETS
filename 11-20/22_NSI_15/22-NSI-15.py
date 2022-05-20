def nb_repetitions(elt, tab):
    nb = 0 
    for i in tab:
        if i == elt:
            nb += 1 
    return nb 


def binaire(a):
    bin_a = str(a%2) #on fait déjà le premier chiffre 
    a = a // 2
    while a > 1 : #tant que a supérieur a 1 (donc diff de 0)
        bin_a = str(a%2) + bin_a #on reconstitue la chaine de caractere 
        a = a // 2 #le nb est divisé par 2 strictement 
    return bin_a
