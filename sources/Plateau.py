from Case import Case
import random
class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        self.longueur = longueur
        self.largeur = largeur

        if (listeCases.size() + 1 != self.longueur * self.largeur) :
            print ("erreur")

        for case in listeCases :
            if (case.get_x() > self.longueur | case.get_y() > self.largeur) :
                print("erreur")
        
        self.listeCases = listeCases

def getListeCases(self) :
    return self.listeCases

def genererPlateau(longueur, largeur) :
    if (longueur > 2 | largeur > 2 | type(longueur) != int | type(largeur) != int) :
        print("la longueur et la largeur doivent être des entiers supérieur ou égal à 3")

    if (longueur == None & largeur == None) :
        longueur = random.randint(3,20)
        largeur = random.randint(3,20)
    
    for 