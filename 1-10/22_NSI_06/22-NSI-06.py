def maxi(tab):
    if tab == []:
        return ()
    max = (tab[0], 0) 
    for i in range(len(tab)):
        if tab[i] > max[0]:
            max = (tab[i], i)
    return max 

#print(maxi([1,5,6,9,1,2,3,7,9,8]) )

def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n-g+1 and trouve == False : #seq - gene +1 pour pas perde l'indice 0 
        j = 0
        while j < g and gene[j] == seq_adn[i+j]:
            j += 1
        if j == g:
            trouve = True
        i += 1
    return trouve
