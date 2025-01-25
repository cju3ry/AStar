class Point:
    def __init__(self, x, y, mur=False, depart=False, arrive=False):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.mur = mur
        self.depart = depart
        self.arrive = arrive

    def calcul_heuristique(self, arrive):
        self.h = abs(self.x - arrive.x) + abs(self.y - arrive.y)

    def calcul_f(self):
        self.f = self.g + self.h

    def set_g(self, valeur_g):
        self.g = valeur_g
        self.calcul_f()

    def __repr__(self):
        """
        Représentation textuelle du point pour le débogage.
        """
        return (f"Point(x={self.x}, y={self.y}, g={self.g}, h={self.h}, f={self.f}, "
                f"mur={self.mur}, depart={self.depart}, arrive={self.arrive})")

# Exemple d'utilisation
if __name__ == "__main__":
    start = Point(0, 0, depart=True)
    end = Point(5, 5, arrive=True)
    wall = Point(2, 2, mur=True)

    # Définir des coûts pour un point
    point = Point(1, 1)
    point.set_g(10)  # Exemple de coût pour arriver à ce point
    point.calcul_heuristique(end)  # Calcul de l'heuristique
    point.calcul_f()  # Mise à jour du coût total

    print(start)
    print(end)
    print(wall)
    print(point)