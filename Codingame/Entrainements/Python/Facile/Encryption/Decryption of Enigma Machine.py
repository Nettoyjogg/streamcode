import sys
import math

def Passage_rotor(message,rotor1,rotor2): #fonction passage rotor
    message_traduit = ''
    for letter in message: #Pour chaque lettre du massage on la cherche sur le premier rotor et on donne son équivalent dans le second rotor
        index=rotor1.index(letter)
        message_traduit += rotor2[index]
    return message_traduit

def Decalage(alphabet,message,decalage,operation): #fonction représentant le shift
    message_décallé = ''
    compteur = 0
    if operation == 'DECODE': #le shift est tjrs donné positivement donc il faut penser à le prendre dans l'autre sens lors du decodage
        decalage = -decalage
    else :
        pass
    for letter in message: #pour chaque lettre du message on prend l'index dans l'alphabet et on réalise le shift + l'incrément au fur et à mesure
        index=alphabet.index(letter)
        nouvel_index=abs((index+decalage+compteur)%26)
        if operation == 'ENCODE':
            compteur += 1
        else:
            compteur -= 1
        message_décallé += alphabet[nouvel_index]
    return message_décallé



operation = input()
decalage = int(input())
rotors=['ABCDEFGHIJKLMNOPQRSTUVWXYZ'] #tableau contenant les LE ROTOR ALPHABET + 3 rotors
for i in range(3):
    rotor = input()
    rotors.append(rotor)
message = input()
resultat = ''

if operation == 'ENCODE':
    resultat = Decalage(rotors[0],message,decalage,operation) #premier decalage
    resultat = Passage_rotor(resultat,rotors[0],rotors[1])#premier rotor
    resultat = Passage_rotor(resultat,rotors[0],rotors[2])#deuxième rotor
    resultat = Passage_rotor(resultat,rotors[0],rotors[3])#troisième rotor    
    print(resultat)
else : # operation == 'DECODE'
    resultat = Passage_rotor(message,rotors[3],rotors[0])#troisième rotor  
    resultat = Passage_rotor(resultat,rotors[2],rotors[0])#deuxième rotor  
    resultat = Passage_rotor(resultat,rotors[1],rotors[0])#premier rotor
    resultat = Decalage(rotors[0],resultat,decalage,operation) # decalage
    print(resultat)    
