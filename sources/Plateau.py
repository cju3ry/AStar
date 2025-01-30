from Case import Case
import random
class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        self.longueur = longueur
        self.largeur = largeur

        if (len(listeCases) != self.longueur * self.largeur) :
            raise ValueError("Le nombre de case est invalide")

        for case in listeCases :
            if (case.get_x() > self.longueur | case.get_y() > self.largeur) :
                raise ValueError("Une des cases est en dehors du platea")
        
        self.listeCases = listeCases

    def getListeCases(self) :
        return self.listeCases

def genererPlateau(longueur, largeur, tauxDeMur, departArriveeOk : bool) :
    if longueur > 2 | largeur > 2 | type(longueur) != int | type(largeur) != int :
        print("la longueur et la largeur doivent être des entiers supérieur ou égal à 3")

    if longueur == None & largeur == None :
        longueur = random.randint(3,20)
        largeur = random.randint(3,20)

    taillePlateau = longueur * largeur

    if not departArriveeOk :
        emplacementDepart = random.randint(0, taillePlateau)
        emplacementArrivee = random.randint(0, taillePlateau)
        
    chaineEtat = ""
    for i in range(taillePlateau) :
        if (departArriveeOk & i == 0) :
            chaineEtat = 'D'
        elif (departArriveeOk & taillePlateau == i) :
            chaineEtat = chaineEtat + 'A'
        elif (emplacementDepart == i) :
            chaineEtat = chaineEtat + 'D'
        elif (emplacementArrivee == i) :
            chaineEtat = chaineEtat + 'A'
        else :
            tauxDeMur = tauxDeMur/100
            probaAleatoire = random.random()
            if (probaAleatoire <= tauxDeMur) :
                chaineEtat += 'X'
            else:
                chaineEtat += 'O'
