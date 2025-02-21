from Case import Case
from Plateau import Plateau

def majListeAdjacente(caseActuelle, listeAdjacente, Plateau):
    """
    Méthode permettant de récupérer la liste de toutes les cases adjacentes existante de la case actuelle en +-x et +-y
    Paramètre
    – La case Actuelle
    - La liste adjacente déja existent
    - Le plateau
    Return : la liste des cases adjacentes
    """
    xActuel = caseActuelle.get_x()
    yActuel = caseActuelle.get_y()

    if Plateau.rechercheCase(xActuel, yActuel + 1) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel, yActuel + 1))

    if Plateau.rechercheCase(xActuel, yActuel - 1) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel, yActuel - 1,))

    if Plateau.rechercheCase(xActuel + 1, yActuel) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel + 1, yActuel))

    if Plateau.rechercheCase(xActuel - 1, yActuel) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel - 1, yActuel))

    return listeAdjacente


def choixSuivant(caseActuelle, Plateau, listeOuverte, listeFerme, caseFin, heuristique):
    """
    Méthode permettant de calculer le plus court chemin en fonction de l'heuristique choisie

    Arguments
    – caseActuelle : la case courante
    - Plateau : le plateau initialisé 
    — listeOuverte : la liste des cases que l'on doit parcourir
    — listeFerme : la liste avec toutes les cases déjà parcourues
    — caseFin : la case de fin ("A").
    - Chemin : la liste des cases avec lesquelles on est passés
    — heuristique : l'heuristique choisie

    """

    if caseActuelle not in listeOuverte:
        listeOuverte.append(caseActuelle)

    # Tant que la liste ouverte n'est pas vide
    while listeOuverte:

        # On trie la liste ouverte par f et g dans l'ordre croissant 
        listeOuverte.sort(key=lambda case: (case.get_f(), case.get_h()))

        # On récupère la première case de la liste (valeur de f et g la plus faible)
        caseActuelle = listeOuverte[0]

        # Ajout de la case actuelle à la liste fermée pour ne pas y repasser.
        listeFerme.append(caseActuelle)

        # Si la case actuelle correspond a la case de fin
        if caseActuelle == caseFin:
            cheminFinal = []

            # Tant qu'il existe une case actuelle, on ajoute la case actuelle au chemin final et on prend son prédécesseur. 
            while caseActuelle:
                cheminFinal.append(caseActuelle)
                caseActuelle = caseActuelle.get_predecesseur()
            
            return cheminFinal, listeFerme

        # Suppression de la première case de la liste ouverte.
        listeOuverte.pop(0)

        # Mise à jour de la liste d'adjacence
        listeAdjacente = majListeAdjacente(caseActuelle, [], Plateau)

        # On parcourt la liste d'adjacence
        for adjacent in listeAdjacente:
            if adjacent not in listeFerme:

                if adjacent not in listeOuverte :

                    # Si la case n'est pas dans la liste ouverte, , le nouveau g, et f, enfin, on modifie le prédecesseur.

                    nouveau_g = caseActuelle.get_g() + 1 # on calcule le nouveau g
                    adjacent.set_g(nouveau_g)  # on set le nouveau g
                    adjacent.calcul_heuristique(caseFin, heuristique) #on calcule l'heuristique en fonction de celle choisie
                    adjacent.calcul_f() #mise à jour de f après la modif de g et h
                    adjacent.set_predecesseur(caseActuelle) # création des prédécesseurs avec la case actuelle comme prédécesseur de la future case (adjascent)
                    listeOuverte.append(adjacent) # ajout dans la liste ouverte, car a traité

    return [], []   # On retourne deux tableaux vides, si aucune solution n'est trouvée.