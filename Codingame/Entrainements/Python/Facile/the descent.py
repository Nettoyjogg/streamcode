import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    l_h = [] #tableau vide qui prendra les valeurs des hauteurs des montagnes
    for i in range(8):
        m_h = int(input())  #taille de la montagne à un point donné
        l_h.append(m_h) #on ajoute la taille de la montagne à la fin de notre tableau de valeur
    h_max=max(l_h)
    index_max=l_h.index(h_max)
    print(index_max)
