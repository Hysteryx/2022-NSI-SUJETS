def recherche(elt,tab):
  for i in range(len(tab)):
    if tab[i] == elt:
      return i 
  return -1 

print(recherche(1, [2, 3, 4,1]))

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2 
    while a < l[i] and i >= 0: 
      l[i+1] = l[i]
      l[i] = a
      i = i - 1 
    return l
