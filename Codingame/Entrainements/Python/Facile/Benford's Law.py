import sys
import math
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
resultat = "false"
nbretransaction = int(input())
bibliotransac = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
tableauLawBenford = {"1":30.1,"2":17.6,"3":12.5,"4":9.7,"5":7.9,"6":6.7,"7":5.8,"8":5.1,"9":4.6}
for i in range(nbretransaction):
    transaction = input()
    x = re.search(r"[1-9]", transaction)
    #print(x[0])
    bibliotransac[x[0]]+=1
for k in bibliotransac:
    bibliotransac[k] = bibliotransac[k]*100/nbretransaction
    if tableauLawBenford[k]-10 <= bibliotransac[k] <= tableauLawBenford[k]+10:
        pass
    else:
        resultat="true"
        break
#print(bibliotransac)
print(resultat)
