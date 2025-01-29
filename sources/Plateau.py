class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        self.longueur = longueur
        self.largeur = largeur

        if (listeCases.size() + 1 != self.longueur * self.largeur) :
            print ("erreur")

        for case in listeCases :
            if (case.getX() > self.longueur | case.getY() > self.largeur) :
                print("erreur")
        
        self.listeCases = listeCases

    