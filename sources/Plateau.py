from Case import Case
import random
class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        self.longueur = longueur
        self.largeur = largeur
        self.cases_dico = {}
        self.total = self.longueur * self.largeur

        if len(listeCases) != self.total:
            raise ValueError("Le nombre de cases ne correspond pas à la taille du plateau")

        for case in listeCases:
            if case.get_x() > self.longueur or case.get_y() > self.largeur:
                raise ValueError("Les coordonnées de la case ne sont pas dans le plateau")
            self.cases_dico[(case.get_x(), case.get_y())] = case

    def getListeCases(self):
        return list(self.cases_dico.values())

    def rechercheCase(self, x, y):
        case = self.cases_dico.get((x, y), None)
        if case and case.get_char() != 'X':
            return case
        return 0

    def getDepart(self):
        for case in self.cases_dico.values():
            if case.get_char() == 'D':
                return case

    def getArrivee(self):
        for case in self.cases_dico.values():
            if case.get_char() == 'A':
                return case

    def afficherPlateau(self):
        # Création de la grille à afficher
        grille = [[' ' for _ in range(self.largeur)] for _ in range(self.longueur)]

        # Remplir la grille avec les caractères des cases
        for case in self.cases_dico.values():
            grille[case.get_x()][case.get_y()] = case.get_char()

        # Affichage de la grille
        for ligne in grille:
            print(" ".join(ligne))

    def dessinerChemin(self, chemin, historique):
        for case in historique:
            if case not in chemin and case.get_char() not in ['D', 'A', 'X']:
                case.char = '*'

        for case in chemin:
            if case.get_char() not in ['D', 'A', 'X']:
                case.char = '.'

    def get_chaine(self):
        chaine = ""
        for case in self.getListeCases() :
            chaine += case.get_char()
        return chaine



# Fonction pour générer un plateau avec un taux de mur et une configuration de départ/arrivée
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
