from  math import *
class Case:
    def __init__(self, x, y, char):
        """
        Création du constructeur de la classe case
        Arguments : 
        - x et y => les coordonées
        - char => le charactère de la case
        
        """
        if x < 0 or y < 0:
            raise ValueError("Les valeurs des coordonnées (x et y) ne doivent pas être négatives !")

        if char not in {"O", "X", "D", "A"}:
            raise ValueError(f"Caractère non conforme : {char}. Attendu : 'O', 'X', 'D' ou 'A'.")

        self.x = x
        self.y = y
        self.g = 0 # Le plus court chemin depuis le départ
        self.h = 0 # L'heuristique depuis la case
        self.f = 0 # L'addition de g et h 
        self.char = char
        self.predecesseur = None # Case dont laquelle la case actuelle est fille 

    def calcul_heuristique(self, arrive, heuristique):
        """
        Méthode permettant le  calcul de l'heuristique en fonction de celle choisit
        Argumment : 
        - arrive => la case d'arrivée
        - heuristique => un charactère représentant l'heuristique chosit (v,d ou e)
        """
        if heuristique == "v":
            self.h = abs(self.x - arrive.x) + abs(self.y - arrive.y)
        elif heuristique == "e":
            self.h = sqrt((self.x - arrive.x) ** 2 + (self.y - arrive.y) ** 2)
        elif heuristique == "d":
            self.h = 0
        else :
            raise ValueError(f"Caractère non conforme : {heuristique}. Attendu : 'v', 'e' ou 'd'.")


    def calcul_f(self):
        self.f = self.g + self.h

    def set_g(self, valeur_g):
        self.g = valeur_g
        self.calcul_f()     #TODO a enlever

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_predecesseur(self, case):
        self.predecesseur = case

    def get_predecesseur(self):
        return self.predecesseur
    
    def get_char(self) :
        return self.char
        
    def get_f(self):
        return self.f

    def get_h(self):
        return self.h

    def get_g(self):
        return self.g