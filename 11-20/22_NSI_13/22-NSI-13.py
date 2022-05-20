def rendu(somme):
    piece_dispo = [5,2,1]
    res = [0,0,0]
    while somme != 0:
        for i in range(len(piece_dispo)):
            if piece_dispo[i] <= somme:
                res[i] += 1 
                somme -= piece_dispo[i]
                break
    return res 

print(rendu(89))

class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element) #on creer obj maillon 
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon #le dernier qui est None on lui met le nouveau maillon 

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None : #tant que y a des maillons 
            print(maillon.valeur)
            maillon = maillon.suivant #on l'envoie vers celui qui est lié a l'actuel 

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file #on prend le dernier 
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur  #on prend la valeur mtn que on a le maillon 
            maillon.suivant = None
            return resultat
        return None 
