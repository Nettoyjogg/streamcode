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

def diviseparset(game:str):
    num_essai=game.split(':')[0].split()[1]
    tab_partie_jeu=game.split(':')[1].split(';')
    tab_essai=[]
    for elem in tab_partie_jeu:
        tab_essai.append(elem.split(','))
    return num_essai,tab_essai

def valeurs_par_set(sets:list):
    green=0
    blue=0
    red=0
    for elem in sets:
        set=elem[1:].split(' ')
        if set[1]=='green':
            green=int(set[0])
        elif set[1]=='blue':
            blue=int(set[0])
        else:
            red=int(set[0])
    return blue,red,green

#Part1 somme des possible
redmax=12
greenmax=13
bluemax=14
resultat=0
tabimpossible=[]
for game in tabfichier:
    essai,tabessai=diviseparset(game)
    #print("essai",essai)
    for set in tabessai:
        blue,red,green=valeurs_par_set(set)
        #print("set",set,"b",blue,"r",red,"g",green)
        if blue>bluemax or red >redmax or green>greenmax:
            tabimpossible.append(int(essai))
            break
somme_game=0
for i in range (1,len(tabfichier)+1):
    somme_game+=i
resultat=somme_game-sum(tabimpossible)
print(tabimpossible)
#print(tabfichier[0].split(':')[1].split(';'))
print("resultatP1 =",resultat)


#Part2 somme puissance des couleurs possible
resultatP2=0
for game in tabfichier:
    essai,tabessai=diviseparset(game)
    bluemin=1
    redmin=1
    greenmin=1
    #print("essai",essai)
    for set in tabessai:
        blue,red,green=valeurs_par_set(set)
        if bluemin<blue:
            bluemin=blue
        if greenmin<green:
            greenmin=green 
        if redmin<red:
            redmin=red
    resultatP2+=redmin*greenmin*bluemin
print("resultatP2 =",resultatP2)