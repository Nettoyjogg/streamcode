import sys
import math

cat_speed = int(input())
message="Escaping the cat"
p1,p2=True,False
trajx,trajy=0,0
# game loop
while True:
    while p1:
        mouse_x, mouse_y, cat_x, cat_y = [int(i) for i in input().split()]
        if -350<cat_x<350:#des que le chat a suffisament commencé à bougé (conc se rapproche de notre sortie)
            trajx=math.ceil(mouse_x/2)
            if cat_y>0:
                trajy=-515
            else:
                trajy=515
            p2=True
            p1=False
        print(-cat_x*2,-cat_y*2,message) #Première strat on vise le point opposé au chat

    while p2:
        print(trajx,trajy,message) #Une fois le chat lancé on vise en ligne droite verticale le point le plus loin du chat
