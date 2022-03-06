import sys
import math

def calcul_distance(longA,latA,longB,latB):
    #transfo donne degrées en radian
    longA=(longA*math.pi)/180
    longB=(longB*math.pi)/180
    latA=(latA*math.pi)/180
    latB=(latB*math.pi)/180

    x=(longB-longA)*math.cos((latA+latB)/2)
    y=latB-latA
    d=math.sqrt((x**2)+(y**2))*6371
    return d

lon = input()
lon=float(lon.replace(',','.'))
lat = input()
lat=float(lat.replace(',','.'))
lieu = ['nul',0] #resultat nom place + distance utilisateur 
n = int(input())
for i in range(n):
    defib = input()
    infos_defib=defib.split(';')
    lond=infos_defib[4]#longitude defibrilateur
    lond=float(lond.replace(',','.'))#on transforme le string retransformé en float
    latd=infos_defib[5]#lat defib
    latd=float(latd.replace(',','.'))
    d=calcul_distance(lond,latd,lon,lat)
    if d < lieu[1] or lieu[0]=='nul':
        lieu[0]=infos_defib[1]
        lieu[1]=d
    else:
        pass
print(lieu[0])
