import sys
import math

# lx: La position de l'éclair sur X
# ly: La position de l'éclair sur Y
# tx: La position de Thor sur X
# ty: La position de Thor sur Y
lx, ly, tx, ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input()) #Nombre de tour de jeu
    #On gère l'axe X
    if lx>tx:
        move_x = "E"
        tx+=1
    elif lx<tx:
        move_x = "W"
        tx-=1
    else:
        move_x = ""
    #On gère l'axe Y
    if ly>ty:
        move_y = "S"
        ty+=1
    elif ly<ty:
        move_y = "N"
        ty-=1
    else:
        move_y = ""

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move_y+move_x)
