from Case import Case
from Plateau import Plateau, genererPlateau
from AStar import trouverFin, trouverDebut, majListeAdjacente, choixSuivant
# Create a list of Case objects
cases = [
    Case(0, 0, 'D'),
    Case(0, 1, 'O'),
    Case(0, 2, 'O'),
    Case(0, 3, 'X'),
    Case(0, 4, 'X'),
    Case(0, 5, 'X'),
    Case(0, 6, 'O'),
    Case(0, 7, 'A'),

    Case(1, 0, 'O'),
    Case(1, 1, 'O'),
    Case(1, 2, 'X'),
    Case(1, 3, 'O'),
    Case(1, 4, 'O'),
    Case(1, 5, 'O'),
    Case(1, 6, 'O'),
    Case(1, 7, 'O'),


    Case(2, 0, 'O'),
    Case(2, 1, 'X'),
    Case(2, 2, 'X'),
    Case(2, 3, 'O'),
    Case(2, 4, 'X'),
    Case(2, 5, 'O'),
    Case(2, 6, 'X'),
    Case(2, 7, 'X'),

    Case(3, 0, 'O'),
    Case(3, 1, 'O'),
    Case(3, 2, 'O'),
    Case(3, 3, 'O'),
    Case(3, 4, 'X'),
    Case(3, 5, 'O'),
    Case(3, 6, 'O'),
    Case(3, 7, 'O'),
]

# Create a Plateau object
plateau = Plateau(4, 8, cases)

# Print the attributes of the Plateau object
print(f"Longueur: {plateau.longueur}")
print(f"Largeur: {plateau.largeur}")
#print(f"case de départ: {plateau.getListeCases()[0]}")
#print(f"case d'arrivée: {plateau.getListeCases()[8]}")
#print("Liste des cases:")
#for case in plateau.getListeCases():
#    print(case)

#caseActuelle = trouverDebut(plateau.getListeCases())
#caseFin = trouverFin(plateau.getListeCases())
caseActuelle = plateau.getDepart()
caseFin = plateau.getArrivee()
print (f"case de départ: {caseActuelle}")
print (f"case d'arrivée : {caseFin}")

listeAdjacente = []
listeCase = plateau.getListeCases()
listeOuverte = []
listeFerme = []
chemin = []
cheminAPrendre = choixSuivant(caseActuelle, listeAdjacente, listeCase, plateau, listeOuverte, listeFerme, caseFin, chemin)
for case in plateau.getListeCases():
    print(case)
print (f"chemin à prendre : {cheminAPrendre}")
for case in plateau.getListeCases():
    print(case)
plateau.dessinerChemin(cheminAPrendre)
plateau.afficherPlateau()
test1 = Case (0,1, "O")
arrive = Case (0,7, "A")
test = test1.calcul_heuristique(arrive)
print(test)