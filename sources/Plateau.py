from Case import Case
import random

class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        self.longueur = longueur  # Nombre de colonnes
        self.largeur = largeur  # Nombre de lignes
        self.cases_dico = {}
        self.total = self.longueur * self.largeur

        if len(listeCases) != self.total:
            print("Test : " + str(self.total) + "l" + str(longueur) + "L" + str(largeur))
            raise ValueError("Le nombre de cases ne correspond pas à la taille du plateau")

        for case in listeCases:
            x, y = case.get_x(), case.get_y()
            if x >= self.longueur or y >= self.largeur:  # Vérification correcte des limites
                raise ValueError("Les coordonnées de la case ne sont pas dans le plateau")
            self.cases_dico[(x, y)] = case

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
        # Initialisation correcte de la grille (largeur = lignes, longueur = colonnes)
        grille = [[' ' for _ in range(self.longueur)] for _ in range(self.largeur)]

        # Remplissage de la grille avec les caractères des cases
        for case in self.cases_dico.values():
            x, y = case.get_x(), case.get_y()
            grille[y][x] = case.get_char()  # y = ligne, x = colonne

        # Affichage de la grille ligne par ligne
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
        return "".join(case.get_char() for case in self.getListeCases())

# Fonction pour générer un plateau avec un taux de mur et une configuration de départ/arrivée
def genererPlateau(longueur, largeur, tauxDeMur, departArriveeOk: bool):
    if longueur < 3 or largeur < 3 or not isinstance(longueur, int) or not isinstance(largeur, int):
        raise ValueError("La longueur et la largeur doivent être des entiers supérieurs ou égaux à 3")

    taillePlateau = longueur * largeur
    chaineEtat = ""

    # Placement aléatoire du départ et de l'arrivée
    if not departArriveeOk:
        emplacementDepart = random.randint(0, taillePlateau - 1)
        emplacementArrivee = random.randint(0, taillePlateau - 1)

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
            chaineEtat += 'X' if random.randint(0, 100) < tauxDeMur else 'O'

    return chaineEtat
