message = input()
#transformation du string en sa valeur numérique puis transfo de decimal à binaire , les transo se font charactère par charactère
message_bin=''
for lettre in message:
    message_bin += bin(ord(lettre))[2:].zfill(7)

resultat=''
boolean = True #si 1 True si 0 False

if message_bin[0]=='0':
    boolean = False
    resultat+='00 0'
else:
    resultat+='0 0'

if len(message_bin)==1:
    print(resultat)
else:

    for chiffre in message_bin[1:]:
        if chiffre=='0' and boolean == False:
            resultat+='0'
        elif chiffre=='1' and boolean == True:
            resultat+='0' 
        elif chiffre=='0' and boolean == True:
            boolean=False
            resultat+=' 00 0'
        else:
            boolean=True
            resultat+=' 0 0'               


    print(resultat)
