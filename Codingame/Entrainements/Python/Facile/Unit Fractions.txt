import sys
import math



n = int(input())
#Après résolution : x = n + n^2 / (y – n)
for y in range (n+1,n**2+n+1):
    #x =(n + n**2)//(y-n)
    x = n*y//(y-n)
    if y>x:
        break
    if n*y%(y-n)==0:
        print(f"1/{n} = 1/{x} + 1/{y}")

