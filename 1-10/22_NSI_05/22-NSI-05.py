def RechercheMinMax(tab):
    res = {"min": None, "max": None}
    if tab != []:
        res["min"] = tab[0]
        res["max"] = tab[0]
    for i in tab: 
        if i >= res["max"]:
            res["max"] = i
        else:
            res["min"] = i 
    return res 

tableau = [0, 1, 4, 2, -2, 9, 3, 1, 7, 1] 
print(RechercheMinMax(tableau))
        

class Carte:
    """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, c, v):
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, 
       Valet, Dame, Roi"""
    def getNom(self):
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        for i in range(4): 
            for k in range(13):
                self.contenu.append(Carte(i,k))
	#A compléter

    """Renvoie la Carte qui se trouve à la position donnée"""
    def getCarteAt(self, pos):
        if pos > 0 and pos <= len(self.contenu):
            return self.contenu[pos]
