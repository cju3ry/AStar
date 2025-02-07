import os

from Case import Case
from FileReader import ecriture_plateeu, lecture_plateau
from Plateau import Plateau, genererPlateau
from AStar import choixSuivant


def afficher_menu():
    print("=== Menu de configuration du plateau ===")

    while True:
        a_un_plateau = input("Avez-vous un plateau à entrer? (oui/non): ").strip().lower()
        if a_un_plateau in ['oui', 'non']:
            a_un_plateau = a_un_plateau == 'oui'
            break
        else:
            print("Réponse invalide. Veuillez entrer 'oui' ou 'non'.")

    if a_un_plateau:
        while True:
            fichier_entree = input("Entrez le chemin du fichier contenant le plateau: ")
            if os.path.isfile(fichier_entree):
                break
            else:
                print("Chemin de fichier invalide. Veuillez entrer un chemin valide.")
        taille_x = taille_y = taux_murs = aleatoire = None
    else:
        fichier_entree = None

        while True:
            try:
                taille_x = int(input("Entrez la largeur du plateau (X): "))
                if taille_x > 0:
                    break
                else:
                    print("La largeur doit être un entier positif.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un entier.")

        while True:
            try:
                taille_y = int(input("Entrez la longueur du plateau (Y): "))
                if taille_y > 0:
                    break
                else:
                    print("La longueur doit être un entier positif.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un entier.")

        while True:
            try:
                taux_murs = int(input("Entrez le taux de murs en pourcentage: "))
                if 0 <= taux_murs <= 100:
                    break
                else:
                    print("Le taux de murs doit être entre 0 et 100.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un entier.")

        while True:
            aleatoire = input("Les points de départ et d'arrivée sont-ils placés aléatoirement? (oui/non): ").strip().lower()
            if aleatoire in ['oui', 'non']:
                aleatoire = aleatoire == 'oui'
                break
            else:
                print("Réponse invalide. Veuillez entrer 'oui' ou 'non'.")

    while True:
        heuristique = input("Entrez le type de calcul d'heuristique ('e' pour eclide , 'v' pour Manhattan ou ville, 'd' pour dijkstra): ").strip().lower()
        if heuristique in ['e', 'v', 'd']:
            break
        else:
            print("Réponse invalide. Veuillez entrer 'e', 'v' ou 'd'.")

    while True:
        fichier_avant = input("Entrez l'emplacement du fichier avant résolution: ") + "\plateauGenere.txt"
        if os.path.isdir(os.path.dirname(fichier_avant)):
            break
        else:
            print("Chemin de dossier invalide. Veuillez entrer un chemin valide.")

    while True:
        fichier_apres = input("Entrez l'emplacement du fichier après résolution: ") + "\plateauResolu.txt"
        if os.path.isdir(os.path.dirname(fichier_apres)):
            break
        else:
            print("Chemin de dossier invalide. Veuillez entrer un chemin valide.")

    return a_un_plateau, fichier_entree, taille_x, taille_y, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres

def resoudre_plateau_entre(fichier_entree, fichier_avant, fichier_apres):
    chaine_plateau = lecture_plateau(fichier_entree)
    taille_x = taille_y = int(len(chaine_plateau) ** 0.5)

    # Debugging: Print the generated or read plateau string
    print("Chaine plateau:", chaine_plateau)

    cases = [Case(i // taille_y, i % taille_y, char) for i, char in enumerate(chaine_plateau)]
    plateau = Plateau(taille_x, taille_y, cases)

    # Afficher le plateau généré
    print("Plateau avant résolution:")
    plateau.afficherPlateau()

    # Sauvegarde le plateau avant résolution
    ecriture_plateeu(fichier_avant, chaine_plateau, taille_x)

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
    caseDepart = caseActuelle

    # Recherche du chemin
    try:
        cheminAPrendre, chemin = choixSuivant(caseActuelle, listeAdjacente, listeCase, plateau, listeOuverte, listeFerme, caseFin, chemin, heuristique, caseDepart)
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
    ecriture_plateeu(fichier_apres, plateau.get_chaine(), taille_x)

def resoudre_plateau_genere(taille_x, taille_y, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres):
    # Génére un plateau avec un taux de murs donné
    chaine_plateau = genererPlateau(taille_x, taille_y, taux_murs, not aleatoire)

    # Debugging: Print the generated or read plateau string
    print("Chaine plateau:", chaine_plateau)

    cases = [Case(i // taille_y, i % taille_y, char) for i, char in enumerate(chaine_plateau)]
    plateau = Plateau(taille_x, taille_y, cases)

    # Afficher le plateau généré
    print("Plateau avant résolution:")
    plateau.afficherPlateau()

    # Sauvegarde le plateau avant résolution
    ecriture_plateeu(fichier_avant, chaine_plateau, taille_x)

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
    caseDepart = caseActuelle

    # Recherche du chemin
    try:
        cheminAPrendre, chemin = choixSuivant(caseActuelle, listeAdjacente, listeCase, plateau, listeOuverte, listeFerme, caseFin, chemin, heuristique, caseDepart)
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
    ecriture_plateeu(fichier_apres, plateau.get_chaine(), taille_x)

# Utilisation du menu pour obtenir les paramètres
a_un_plateau, fichier_entree, taille_x, taille_y, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres = afficher_menu()

# Appel de la méthode appropriée en fonction du choix de l'utilisateur
if a_un_plateau:
    resoudre_plateau_entre(fichier_entree, fichier_avant, fichier_apres)
else:
    resoudre_plateau_genere(taille_x, taille_y, taux_murs, heuristique, aleatoire, fichier_avant, fichier_apres)