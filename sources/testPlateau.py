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

# Création du plateau
plateau = Plateau(4, 8, cases)

# Récupération des cases de départ et d'arrivée
caseActuelle = plateau.getDepart()
caseFin = plateau.getArrivee()
print(f"Case de départ: {caseActuelle}")
print(f"Case d'arrivée: {caseFin}")

# Initialisation des listes
listeAdjacente = []
listeCase = plateau.getListeCases()
listeOuverte = []
listeFerme = []
chemin = []
historique = []
heuristique = "e"
caseDepart = caseActuelle

#choixSuivant(caseActuelle, listeAdjacente, listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin, heuristique, caseDepart):

# Recherche du chemin
cheminAPrendre,chemin = choixSuivant(caseActuelle, listeAdjacente, listeCase, plateau, listeOuverte, listeFerme, caseFin, chemin,heuristique, caseDepart)

# Affichage du chemin trouvé
print(f"Chemin à prendre : {cheminAPrendre}")
print(f"Chemin trouvé : {chemin}")

# Marquage du plateau avec le chemin et les cases explorées
plateau.dessinerChemin(cheminAPrendre, chemin)
plateau.afficherPlateau()
