from Case import Case
from Plateau import Plateau, genererPlateau
from AStar import trouverFin, trouverDebut, majListeAdjacente, choixSuivant
import random
import time

from sources.FileReader import FileReader

# Génération d'un plateau 50x50 avec des cases accessibles et obstacles
size = 50
cases = []

# Placement du départ et de l'arrivée
start_x, start_y = 0, 0
end_x, end_y = size - 1, size - 1

for i in range(size):
    for j in range(size):
        if (i, j) == (start_x, start_y):
            cases.append(Case(i, j, 'D'))  # Case de départ
        elif (i, j) == (end_x, end_y):
            cases.append(Case(i, j, 'A'))  # Case d'arrivée
        else:
            cases.append(Case(i, j, 'O' if random.random() > 0.2 else 'X'))  # 20% d'obstacles


file_reader = FileReader("C:\\Users\\clemj\\Downloads\\input_50x50.txt")
characters, total_lines, max_columns = file_reader.analyze_characters()

# Create a Plateau object
plateau = Plateau(total_lines, max_columns, characters)

# Création du plateau
#plateau = Plateau(size, size, cases)

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

# Recherche du chemin
t1 = time.time()
cheminAPrendre, chemin = choixSuivant(caseActuelle, plateau, listeOuverte, listeFerme, caseFin, chemin, heuristique)
t2 = time.time()
print(t2 - t1)

# Affichage du chemin trouvé
print(f"Chemin à prendre : {cheminAPrendre}")
print(f"Chemin trouvé : {chemin}")

#Marquage du plateau avec le chemin et les cases explorées
plateau.dessinerChemin(cheminAPrendre, chemin)
plateau.afficherPlateau()
