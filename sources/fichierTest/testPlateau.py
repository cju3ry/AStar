from Case import Case
from Plateau import Plateau, genererPlateau

# Create a list of Case objects
cases = [
    Case(0, 0, 'D'),
    Case(0, 1, 'O'),
    Case(0, 2, 'X'),
    Case(1, 0, 'O'),
    Case(1, 1, 'X'),
    Case(1, 2, 'O'),
    Case(2, 0, 'X'),
    Case(2, 1, 'O'),
    Case(2, 2, 'A')
]

# Create a Plateau object
plateau = Plateau(3, 3, cases)

# Print the attributes of the Plateau object
print(f"Longueur: {plateau.longueur}")
print(f"Largeur: {plateau.largeur}")
print("Liste des cases:")
for case in plateau.getListeCases():
    print(case)