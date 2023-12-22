def replacedigit(phrase:str):
    un=phrase.find("one")
    deux=phrase.find("two")
    trois=phrase.find("three")
    quatre=phrase.find("four")
    cinq=phrase.find("five")
    six=phrase.find("six")
    sept=phrase.find("seven")
    huit=phrase.find("eight")
    neuf=phrase.find("nine")

    tables=[un,deux,trois,quatre,cinq,six,sept,huit,neuf]
    maxi=len(phrase)
    indice=-1
    for elem in len(tables):
        if tables[elem]!=-1 and tables[elem]<maxi:
            maxi=tables[elem]
            indice=elem
            
    if indice==-1:
        return phrase
    
    


    return phrase

mottest="alzefhbtwo87onethreeightninsixpjazefiveight"
print(mottest.globals())