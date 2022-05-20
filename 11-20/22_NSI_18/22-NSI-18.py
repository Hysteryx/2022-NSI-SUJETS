def mini(t_moy, annees):
    min = (t_moy[0], annees[0])
    for i in range(1,len(t_moy)):
        if min[0] > t_moy[i]:
            min = (t_moy[i], annees[i])
    return min 

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7] 
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(mini(t_moy, annees))

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result 
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse #renvoie boolean 
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)
