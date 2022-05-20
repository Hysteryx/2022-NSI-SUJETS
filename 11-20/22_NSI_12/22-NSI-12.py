def moyenne(tab):
    if tab == []:
        return 'Erreur'
    prov = 0 
    for i in tab:
        prov += i 
    return prov/len(tab)

def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i= 0
    j= len(tab)
    while i != j :
        if tab[i]== 0:
            i= i + 1 
        else :
            valeur = tab[j]
            tab[j] = tab[i]
            tab[i] = valeur 
            j= j - 1 
    return tab 
