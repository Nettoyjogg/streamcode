import sys
import math

#On crée notre langue pour arriver à faire correspondre les demande de vin, et les noms des caisse
#notre langue ici est un tableau de chiffre , chaque chiffre correspond à une lettre d'un alphabet traduit

def ajoutentreetraduite(entree: str,listdetraduction:list,listalphabet:list):
    entreetraduite=[]#tableau qui donne l'equivalent de l'entree en tableau chiffree
    for lettre in entree:
        if lettre not in listalphabet:
            listalphabet.append(lettre)
        entreetraduite+=[listalphabet.index(lettre)]
    listdetraduction.append(entreetraduite)
    return listdetraduction


n = int(input())

tabrequest=[] #tableau de requete de vin traduite dans notre langue 
tabcrate=[] #tableau de caisse traduite dans notre langue 
for i in range(n): #On cree le tableau de requete de vin traduite dans notre alphabet de chiffre
    tablettre=[]
    request = input()
    tabrequest=ajoutentreetraduite(request,tabrequest,tablettre)

for i in range(n): #On cree le tableau de caisse traduite dans notre alphabet de chiffre
    tablettre=[]
    crate = input()
    tabcrate=ajoutentreetraduite(crate,tabcrate,tablettre)

for i in range(n): #On sort le numéro de la caisse correspondant à le demande de vin
    for j in range(0,len(tabcrate)):
        if tabrequest[i] == tabcrate[j]:
            print(j+1)
        else:
            pass


