import os

from Case import Case
from FileReader import ecriture_plateau, lecture_plateau
from Plateau import Plateau, genererPlateau
from AStar import choixSuivant

import os

def afficher_menu():
    print("=== Menu de configuration du plateau ===")

    a_un_plateau = input("Avez-vous un plateau à entrer? (oui/non): ").strip().lower()
    while a_un_plateau not in ['oui', 'non']:
        print("Réponse invalide. Veuillez entrer 'oui' ou 'non'.")
        a_un_plateau = input("Avez-vous un plateau à entrer? (oui/non): ").strip().lower()
    a_un_plateau = a_un_plateau == 'oui'

    if a_un_plateau:
        fichier_entree = input("Entrez le chemin du fichier contenant le plateau: ")
        while not os.path.isfile(fichier_entree):
            print("Chemin de fichier invalide. Veuillez entrer un chemin valide.")
            fichier_entree = input("Entrez le chemin du fichier contenant le plateau: ")
        taille_x = taille_y = taux_murs = aleatoire = None
    else:
        fichier_entree = None

        taille_y = input("Entrez le nombre de colonnes du plateau (Y): ")
        while not taille_y.isdigit() or int(taille_y) <= 0:
            print("La largeur doit être un entier positif.")
            taille_y = input("Entrez le nombre de colonnes du plateau (Y): ")
        taille_y = int(taille_y)

        taille_x = input("Entrez le nombre de lignes du plateau (X): ")
        while not taille_x.isdigit() or int(taille_x) <= 0:
            print("La longueur doit être un entier positif.")
            taille_x = input("Entrez le nombre de lignes du plateau (X): ")
        taille_x = int(taille_x)

        taux_murs = input("Entrez le taux de murs en pourcentage: ")
        while not taux_murs.isdigit() or not (0 <= int(taux_murs) <= 100):
            print("Le taux de murs doit être entre 0 et 100.")
            taux_murs = input("Entrez le taux de murs en pourcentage: ")
        taux_murs = int(taux_murs)

        aleatoire = input("Les points de départ et d'arrivée sont-ils placés aléatoirement? (oui/non): ").strip().lower()
        while aleatoire not in ['oui', 'non']:
            print("Réponse invalide. Veuillez entrer 'oui' ou 'non'.")
            aleatoire = input("Les points de départ et d'arrivée sont-ils placés aléatoirement? (oui/non): ").strip().lower()
        aleatoire = aleatoire == 'oui'

    heuristique = input("Entrez le type de calcul d'heuristique ('e' pour eclide , 'v' pour Manhattan ou ville, 'd' pour dijkstra): ").strip().lower()
    while heuristique not in ['e', 'v', 'd']:
        print("Réponse invalide. Veuillez entrer 'e', 'v' ou 'd'.")
        heuristique = input("Entrez le type de calcul d'heuristique ('e' pour eclide , 'v' pour Manhattan ou ville, 'd' pour dijkstra): ").strip().lower()

    fichier_avant = input("Entrez l'emplacement du fichier avant résolution: ") + "/plateauGenere.txt"
    while not os.path.isdir(os.path.dirname(fichier_avant)):
        print("Chemin de dossier invalide. Veuillez entrer un chemin valide.")
        fichier_avant = input("Entrez l'emplacement du fichier avant résolution: ") + "/plateauGenere.txt"

    fichier_apres = input("Entrez l'emplacement du fichier après résolution: ") + "/plateauResolu.txt"
    while not os.path.isdir(os.path.dirname(fichier_apres)):
        print("Chemin de dossier invalide. Veuillez entrer un chemin valide.")
        fichier_apres = input("Entrez l'emplacement du fichier après résolution: ") + "/plateauResolu.txt"

    return a_un_plateau, fichier_entree, taille_y, taille_x, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres

def resoudre_plateau_entre(fichier_entree, fichier_avant, fichier_apres):
    chaine_plateau, taille_y, taille_x  = lecture_plateau(fichier_entree)

    print("Chaine plateau:", chaine_plateau)

    cases = []
    for i, char in enumerate(chaine_plateau):
        y = i // taille_x  # Calcule la ligne
        x = i % taille_x   # Calcule la colonne
        cases.append(Case(x, y, char))  # Création de l'objet Case et ajout à la liste

    plateau = Plateau(taille_x, taille_y, cases)

    # Afficher le plateau généré
    print("Plateau avant résolution:")
    plateau.afficherPlateau()

    # Sauvegarde le plateau avant résolution
    ecriture_plateau(fichier_avant, chaine_plateau, taille_x)

    # Récupération des cases de départ et d'arrivée
    caseActuelle = plateau.getDepart()
    caseFin = plateau.getArrivee()
    print(f"Case de départ: {caseActuelle}")
    print(f"Case d'arrivée: {caseFin}")

    # Initialisation des listes
    listeOuverte = []
    listeFerme = []

    # Recherche du chemin
    try:
        cheminAPrendre, chemin = choixSuivant(caseActuelle, plateau, listeOuverte, listeFerme, caseFin, heuristique)

        # TODO rajouter le if si pas de chemin 
    except RecursionError:
        print("RecursionError: maximum recursion depth exceeded. Retrying...")
        return None

    # Affichage du chemin trouvé
    print(f"Chemin à prendre : {cheminAPrendre}")
    print(f"Chemin trouvé : {chemin}")

    # Marquage du plateau avec le chemin et les cases explorées
    plateau.dessinerChemin(cheminAPrendre, chemin)

    # Afficher le plateau après résolution
    print("Plateau après résolution:")
    plateau.afficherPlateau()

    # Sauvegarder le plateau après résolution
    ecriture_plateau(fichier_apres, plateau.get_chaine(), taille_x)

def resoudre_plateau_genere(taille_x, taille_y, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres):
    # Génére un plateau avec un taux de murs donné
    chaine_plateau = genererPlateau(taille_y, taille_x, taux_murs, not aleatoire)

    print("Chaine plateau:", chaine_plateau)

    cases = [Case(i % taille_x, i // taille_x, char) for i, char in enumerate(chaine_plateau)]  # Correction des coordonnées
    plateau = Plateau(taille_x, taille_y, cases)

    # Afficher le plateau généré
    print("Plateau avant résolution:")
    plateau.afficherPlateau()

    # Sauvegarde le plateau avant résolution
    ecriture_plateau(fichier_avant, chaine_plateau, taille_x)

    # Récupération des cases de départ et d'arrivée
    caseActuelle = plateau.getDepart()
    caseFin = plateau.getArrivee()

    # Initialisation des listes
    listeOuverte = []
    listeFerme = []

    # Recherche du chemin
    try:
        cheminAPrendre, chemin = choixSuivant(caseActuelle, plateau, listeOuverte, listeFerme, caseFin, heuristique)
        if len(cheminAPrendre) == 0 and len(chemin) == 0:
            print ("Aucun chemin possible !!")
            return None
    except RecursionError:
        print("RecursionError: maximum recursion depth exceeded. Retrying...")
        return None

    # Affichage du chemin trouvé
    print(f"Chemin à prendre : {cheminAPrendre}")
    print(f"Chemin trouvé : {chemin}")

    # Marquage du plateau avec le chemin et les cases explorées
    plateau.dessinerChemin(cheminAPrendre, chemin)

    # Afficher le plateau après résolution
    print("Plateau après résolution:")
    plateau.afficherPlateau()

    # Sauvegarder le plateau après résolution
    print(plateau.get_chaine())
    print(taille_x)
    ecriture_plateau(fichier_apres, plateau.get_chaine(), taille_x)

# Utilisation du menu pour obtenir les paramètres
a_un_plateau, fichier_entree, taille_x, taille_y, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres = afficher_menu()

# Vérification des tailles avant d'appeler les fonctions
print(f"taille_x = {taille_x}, taille_y = {taille_y}")

# Appel de la méthode appropriée en fonction du choix de l'utilisateur
if a_un_plateau:
    resoudre_plateau_entre(fichier_entree, fichier_avant, fichier_apres)
else:
    resoudre_plateau_genere(taille_x, taille_y, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres)
