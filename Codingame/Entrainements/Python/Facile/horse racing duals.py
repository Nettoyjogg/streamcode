import sys
import math


n = int(input()) #Nombre de chevaux
l_c=[] #liste des chevaux
l_e=[] #liste des ecarts de puissance
for i in range(n):
    cheval = int(input())
    l_c.append(cheval) #On ajoute le cheval à la liste
l_c.sort() #on tri la liste
l_e=[l_c[c+1] - l_c[c] for c in range(len(l_c) -1)] #Dans notre liste liste ecart on calcule pour 
#chaque cheval la diff entre le cheval supp et lui meme . le range prend un -1 car pas besoin de différence pour le cheval le plus puissant
resultat=min(l_e) #le resultat est alors l'écart min
print(resultat)
