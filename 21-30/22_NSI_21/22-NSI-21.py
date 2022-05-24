def multiplication(n1, n2):
    if n1 < 0:
        return -multiplication(-n1, n2)
    if n2 < 0:
        return -multiplication(n1, -n2)
    res = 0 
    for i in range(n1):
        res += n2 
    return res 

print(multiplication(-2,6))

def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2 
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1		
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))

