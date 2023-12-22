import os
#Récupération de l'input avec un chemin relatif
absolute_path = os.path.dirname(os.path.abspath(__file__))
fichier = open(absolute_path+"/input.txt", "r")

#transformation de l'input pour avoir une liste de chaque ligne sans retour à la ligne
tabfichier = fichier.readlines()
fichier.close()
for i,element in enumerate(tabfichier[:-1]) :
    element = element[:-1]
    tabfichier[i]=element

redmax=12
greenmax=13
bluemax=14
resultat=0

def diviseparset(tabfic:str):
    essai=tabfic.split(':')[0].split()[1]
    tabdivise=tabfic.split(':')[1]
    return tabdivise

#Part1
tabpossible=[]


print(tabfichier[0].split(':')[1])