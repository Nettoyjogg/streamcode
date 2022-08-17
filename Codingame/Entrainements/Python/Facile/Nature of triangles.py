import sys
import math

def vecteur(x_a,y_a,x_b,y_b):
    return (x_b-x_a,y_b-y_a)

def longueur(vec1:tuple):
    return math.sqrt(vec1[0]**2+vec1[1]**2)

def find_nature_side(AB,AC,BC,a,b,c):
    if AB!=AC and AB!=BC and AC!=BC:
        return 'scalene',0
    elif AB==AC and AC!=BC:
        return 'isosceles',a
    elif AB==BC and AC!=BC:
        return 'isosceles',b
    elif AC==BC and AB!=AC:
        return 'isosceles',c
    else:
        return "equilateral",0

def calculangle(vec1:tuple,vec2:tuple,vec3:tuple,AB,AC,BC):
    cos_angle1=(vec1[0]*vec2[0]+vec1[1]*vec2[1])/(AB*AC)
    angle1=math.acos(cos_angle1)*180/math.pi
    cos_angle2=(-vec1[0]*vec3[0]+(-vec1[1])*vec3[1])/(AB*BC)
    angle2=math.acos(cos_angle2)*180/math.pi
    cos_angle3=(vec2[0]*vec3[0]+vec2[1]*vec3[1])/(AC*BC)
    angle3=math.acos(cos_angle3)*180/math.pi

    return angle1,angle2,angle3

def find_angle_nature(a,b,c,angleA,angleB,angleC):
    val=max(angleA,angleB,angleC)
    if val<90:
        return 'acute',0,val
    elif val==90:
        if val==angleA:
            return 'right',a,val
        elif val==angleB:
            return 'right',b,val
        else:
            return 'right',c,val
    else:
        if val==angleA:
            return 'obtuse',a,val
        elif val==angleB:
            return 'obtuse',b,val
        else:
            return 'obtuse',c,val


n = int(input())
for i in range(n):
    inputs = input().split()
    a = inputs[0]
    x_a = int(inputs[1])
    y_a = int(inputs[2])
    b = inputs[3]
    x_b = int(inputs[4])
    y_b = int(inputs[5])
    c = inputs[6]
    x_c = int(inputs[7])
    y_c = int(inputs[8])

    #calcul des 3 vecteurs AB, AC et BC
    vec_ab=vecteur(x_a,y_a,x_b,y_b)
    vec_ac=vecteur(x_a,y_a,x_c,y_c)
    vec_bc=vecteur(x_b,y_b,x_c,y_c)


    #calcul des longueurs des côtés du triangle
    AB=longueur(vec_ab)
    AC=longueur(vec_ac)
    BC=longueur(vec_bc)

    #calcul des anles de chaque côté du triangle
    angleA,angleB,angleC=calculangle(vec_ab,vec_ac,vec_bc,AB,AC,BC)
    #print("AB",AB,"AC",AC,"BC",BC, file=sys.stderr, flush=True)
    #print("angle A",angleA,"angle B",angleB,"angle C",angleC, file=sys.stderr, flush=True)
    #print("vecab",vec_ab,"vecac",vec_ac,"vecbc",vec_bc, file=sys.stderr, flush=True)

    #recherche type de triangle (quelquonque , isocèle ou équi)
    nature_side=find_nature_side(AB,AC,BC,a,b,c)

    #on recherche le type de triangle associé à son angle fort
    angle_nature=find_angle_nature(a,b,c,angleA,angleB,angleC)
    
    #gestion de l'affichage en 2 partie d'abord la nature puis l'angle
    if nature_side[0]=='scalene':
        print(f'{a}{b}{c} is a scalene and ',end='')
    else:
        print(f'{a}{b}{c} is an isosceles in {nature_side[1]} and ',end='')

    if angle_nature[0]=='acute':
        print('an acute triangle.')
    elif angle_nature[0]=='right':
        print(f'a right in {angle_nature[1]} triangle.')   
    else:
        print(f'an obtuse in {angle_nature[1]} ({round(angle_nature[2])}°) triangle.')  

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

