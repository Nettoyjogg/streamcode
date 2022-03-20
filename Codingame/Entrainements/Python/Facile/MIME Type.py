import sys
import math

Bib_asso={}

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    Bib_asso[ext.lower()]=mt #on met toute les clé en lower pour eviter les probleme de casse
#print(Bib_asso)
for i in range(q):
    fname = input()
    #print(fname)
    if '.' in fname:
        listname=fname.split(".")
        if listname[-1].lower() in Bib_asso:
            print(Bib_asso[listname[-1].lower()])
        else:
            print("UNKNOWN")   
    else :
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
        print("UNKNOWN")

