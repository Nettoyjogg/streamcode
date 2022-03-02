import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

for i in range(n):
    compteur=0
    line = input()
    j=0
    while j < len(line) :
        if line[j] == 'f':
            j+= 3
            compteur +=1
        else :
            j+=1
    print(compteur)
