from Case import Case
import random
class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        self.longueur = longueur
        self.largeur = largeur
        total = self.longueur * self.largeur

        if (len(listeCases)) != total :
            raise ValueError("Le nombre de cases ne correspond pas à la taille du plateau")

        for case in listeCases :
            if (case.get_x() > self.longueur or case.get_y() > self.largeur) :
                raise ValueError("Les coordonnées de la case ne sont pas dans le plateau")
        
        self.listeCases = listeCases

    def getListeCases(self) :
        return self.listeCases
    
    def rechercheCase(self, x, y):
        for case in self.listeCases:
            if(case.get_x() == x and case.get_y() == y and case.get_char() != "X"):
                return case
        return 0

    def getDepart(self) :
            for case in self.listeCases :
                if case.get_char() == 'D' :
                    return case

    def getArrivee(self) :
        for case in self.listeCases :
            if case.get_char() == 'A' :
                return case

def genererPlateau(longueur, largeur, tauxDeMur, departArriveeOk: bool):
    if longueur <= 2 or largeur <= 2 or type(longueur) != int or type(largeur) != int:
        raise ValueError("La longueur et la largeur doivent être des entiers supérieurs ou égaux à 3")

    if longueur is None and largeur is None:
        longueur = random.randint(3, 20)
        largeur = random.randint(3, 20)

    taillePlateau = longueur * largeur

    if not departArriveeOk:
        emplacementDepart = random.randint(0, taillePlateau - 1)
        emplacementArrivee = random.randint(0, taillePlateau - 1)

    chaineEtat = ""
    for i in range(taillePlateau):
        if departArriveeOk and i == 0:
            chaineEtat += 'D'
        elif departArriveeOk and i == taillePlateau - 1:
            chaineEtat += 'A'
        elif not departArriveeOk and i == emplacementDepart:
            chaineEtat += 'D'
        elif not departArriveeOk and i == emplacementArrivee:
            chaineEtat += 'A'
        else:
            generationMur = random.randint(0, 100)
            if generationMur < tauxDeMur:
                chaineEtat += 'X'
            else:
                chaineEtat += 'O'
    return chaineEtat
