#compare 2 signe et donne le numéro du signe vainqueur
def combat(num1:int,num2:int,liste_j:list,bib_j:dict,signes:dict):
    sign1=bib_j[num1]['signe']
    sign2=bib_j[num2]['signe']
    vainqueur=0

    if sign1!=sign2:
        if sign2 not in signes[sign1]: #on regarde si le signe 2 est dans les signes vaincus du signe 1
            return num2
        else:
            return num1
    else: #si meme signe plus petit numéro gagne
        vainqueur=min(num1,num2)

    return vainqueur


n = int(input())
bib_joueur={}
signe_vaincu={'R':'LC','C':'LP','L':'SP','S':'RC','P':'RS'} #associe à chaque signe ses signes vaincus
liste_joueur=[]

for i in range(n):
    inputs = input().split()
    numplayer = int(inputs[0])
    signplayer = inputs[1]
    bib_joueur[numplayer]={'signe':inputs[1],'battus':[]}
    liste_joueur.append(numplayer)

while len(liste_joueur)>1: #tant qu'on a pas notre gagnant
    liste_copy=liste_joueur.copy()

    while len(liste_joueur)!=0: #correspond à un tour de jeu
        num1=liste_joueur[0]
        num2=liste_joueur[1]
        vainqueur=combat(num1,num2,liste_joueur,bib_joueur,signe_vaincu)
        if vainqueur==num1:
            liste_copy.remove(num2)
            bib_joueur[num1]['battus'].append(num2)
        else:
            liste_copy.remove(num1)
            bib_joueur[num2]['battus'].append(num1)
        liste_joueur=liste_joueur[2:] #on prend les joueurs 2 à deux du coup on enlève les joueurs qui ont déjà combattu

    liste_joueur=liste_copy.copy()

gagnant=liste_joueur[0]
print(gagnant)
print(*bib_joueur[gagnant]['battus'])
