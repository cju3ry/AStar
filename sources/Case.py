from  math import *
class Case:
    def __init__(self, x, y, char):
        if x < 0 or y < 0:
            raise ValueError("Les valeurs des coordonnées (x et y) ne doivent pas être négatives !")

        if char not in {"O", "X", "D", "A"}:
            raise ValueError(f"Caractère non conforme : {char}. Attendu : 'O', 'X', 'D' ou 'A'.")

        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.char = char
        self.predecesseur = None

    def calcul_heuristique(self, arrive, heuristique):
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
        self.calcul_f()

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