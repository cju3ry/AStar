from Case import Case
import random

class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        """
        Création du constructeur de la classe plateau
        Arguments : 
        - longueur => la longueur du plateau
        - largeur => la largeur du plateau
        - listecases => listes des cases contenu dans le plateau
        """
        self.longueur = longueur
        self.largeur = largeur 
        self.cases_dico = {}
        self.total = self.longueur * self.largeur

        if len(listeCases) != self.total:
            print("Test : " + str(self.total) + "l" + str(longueur) + "L" + str(largeur))
            raise ValueError("Le nombre de cases ne correspond pas à la taille du plateau")

        # Parcours de la liste des cases pouur savoir si la case est bien dans le plateau 
        for case in listeCases:
            x, y = case.get_x(), case.get_y()
            if x >= self.longueur or y >= self.largeur:
                raise ValueError("Les coordonnées de la case ne sont pas dans le plateau")
            # Si la case est valide on l'ajoute dans le dictionnaire avec comme clé les coordonnées x, y
            self.cases_dico[(x, y)] = case

    def getListeCases(self):
        return list(self.cases_dico.values())

    def rechercheCase(self, x, y):
        """ 
        Permet de récupérer une case grâce à ses coordonées x,y du dictionnaire
        Return => la case si elle existe, 0 sinon

        """
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
        # Initialisation de la grille (largeur = lignes, longueur = colonnes)
        grille = [[' ' for _ in range(self.longueur)] for _ in range(self.largeur)]

        # Remplissage de la grille avec les caractères des cases
        for case in self.cases_dico.values():
            x, y = case.get_x(), case.get_y()
            grille[y][x] = case.get_char()

        # Affichage de la grille ligne par ligne
        for ligne in grille:
            print(" ".join(ligne))

    def dessinerChemin(self, chemin, historique):

        """
        Méthode permettant de dessiner le plus court chemin du départ à l'arrivée dans l'invite de commande
        Arguement :  
        - chemin => liste de cases du plus court chemin
        - historique => liste de toutes les cases parcourus
        """
        for case in historique:
            if case not in chemin and case.get_char() not in ['D', 'A', 'X']:
                case.char = '*'

        for case in chemin:
            if case.get_char() not in ['D', 'A', 'X']:
                case.char = '.'


    def get_chaine(self):
        return "".join(case.get_char() for case in self.getListeCases()) # Plateau sous forme  de chaine de caractère (OOOXXA...)


def genererPlateau(longueur, largeur, tauxDeMur, departArriveeOk: bool):
    """
    Fonction pour générer un plateau avec un taux de mur et un départ/arrivée

    Argument :  
    - Longueur du platau
    - Largeur du plateau
    - Le taux de mur que doit comporter le plateau
    - Boolean définnissant si le départ et l'arrivée sont placés au début et à la fin du plateau ou non

    Return : une chaine de caractère qui correspond au plateau
    """

    if longueur < 3 or largeur < 3 or not isinstance(longueur, int) or not isinstance(largeur, int):
        raise ValueError("La longueur et la largeur doivent être des entiers supérieurs ou égaux à 3")

    taillePlateau = longueur * largeur
    chaineEtat = ""

    # Placement aléatoire du départ et de l'arrivée
    if not departArriveeOk:
        emplacementDepart = random.randint(0, taillePlateau - 1)
        emplacementArrivee = random.randint(0, taillePlateau - 1)

    # Construction de la chaine du plateau
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
