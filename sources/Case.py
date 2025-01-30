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

    def calcul_heuristique(self, arrive):
        self.h = abs(self.x - arrive.x) + abs(self.y - arrive.y)

    def calcul_f(self):
        self.f = self.g + self.h

    def set_g(self, valeur_g):
        self.g = valeur_g
        self.calcul_f()

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
