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

    def __repr__(self):
        """
        Représentation textuelle du case pour le débogage.
        """
        return (f"(x={self.x}, y={self.y}, g={self.g}, h={self.h}, f={self.f}, "
                f"char={self.char},)")

# Exemple d'utilisation
if __name__ == "__main__":
    start = Case(0, 0,"D")
    end = Case(5, 5,"A")
    wall = Case(2, 2, "X")

    # Définir des coûts pour un case
    case = Case(1, 1, "O")
    case.set_g(10)  # Exemple de coût pour arriver à ce case
    case.calcul_heuristique(end)  # Calcul de l'heuristique
    case.calcul_f()  # Mise à jour du coût total

    print(start)
    print(end)
    print(wall)
    print(case)