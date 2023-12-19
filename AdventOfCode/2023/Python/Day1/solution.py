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

#fonctions

#Sort le premier nombre d'une chaine de caractère
def first_digit(phrase:str): 
    for letter in phrase:
        if letter.isdigit():
            return letter
    return 0 #si pas de nombre dans la phrase

#Remplace des digits écrit littérallement par leur valeur numérique
def replacedigit(phrase:str):
    phrase=phrase.replace("one","1")
    phrase=phrase.replace("two","2")
    phrase=phrase.replace("three","3")
    phrase=phrase.replace("four","4")
    phrase=phrase.replace("five","5")
    phrase=phrase.replace("six","6")
    phrase=phrase.replace("seven","7")
    phrase=phrase.replace("eight","8")
    phrase=phrase.replace("nine","9")
    return phrase

tableau_calibration=[]
'''
#Part1
for element in tabfichier:
    c1=first_digit(element)
    c2=first_digit(element[::-1])
    tableau_calibration.append(str(c1)+str(c2))
'''
#Part2
for element in tabfichier:
    element_bon=replacedigit(element)
    c1=first_digit(element_bon)
    c2=first_digit(element_bon[::-1])
    tableau_calibration.append(str(c1)+str(c2))
#print(tableau_calibration)
#transformation de la liste de string en liste de int
tableau_calibration=list(map(int,tableau_calibration))

resultat=sum(tableau_calibration)
print(resultat)