def recherche(tab):
    if tab == []:
        return 
    last = tab[0]
    final = []
    for i in range(1,len(tab)):
        if tab[i] == last + 1:
            final.append((last,tab[i]))
        last = tab[i]
    return final 

#print(recherche([5, 1, 2, 3, 8, -5, -4, 7]))

def propager(M, i, j, val):
    if M[i][j]== 0:
        return
    M[i][j]=val
    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):
        propager(M, i-1, j, val)
    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):
        propager(M, i+1, j, val)
    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):
        propager(M, i, j-1, val)
    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1):
        propager(M, i, j+1, val)
