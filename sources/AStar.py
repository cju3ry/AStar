from Case import Case
from Plateau import Plateau

def majListeAdjacente(caseActuelle, listeAdjacente, Plateau):
    """
    Méthode permettant de récupérer la liste de toutes les cases adjascentes existante de la case actuelle
    Paramètre : 
    - La case Actuelle
    - La liste adjacente déja exisitante
    - Le plateau
    Return : la liste des cases adjascentes
    """
    xActuel = caseActuelle.get_x()
    yActuel = caseActuelle.get_y()

    if Plateau.rechercheCase(xActuel + 1, yActuel) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel + 1, yActuel))

    if Plateau.rechercheCase(xActuel - 1, yActuel) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel - 1, yActuel))

    if Plateau.rechercheCase(xActuel, yActuel + 1) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel, yActuel + 1))

    if Plateau.rechercheCase(xActuel, yActuel - 1) != 0:
        listeAdjacente.append(Plateau.rechercheCase(xActuel, yActuel - 1,))

    return listeAdjacente


def choixSuivant(caseActuelle, Plateau, listeOuverte, listeFerme, caseFin, chemin, heuristique):
    """
    Méthode permettant de calculé le plus court chemin en fonction de l'heuristique choisie

    Arguments : 
    - caseActuelle : la case courante 
    - Plateau : le plateau initialisé 
    - listeOuverte : la liste des cases que l'on doit parcourir
    - listeFerme : la liste avec toutes les cases déjà parcourues
    - caseFin : la case de fin ("A")
    - chemin : la liste des cases où ont est passés
    - heuristique : l'heuristique choisie

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
        if caseActuelle not in chemin:  #TODO a enlever
            chemin.append(caseActuelle)

        # Si la case actuelle correspond a la case de fin
        if caseActuelle == caseFin:
            cheminFinal = []

            # Tant qu'il existe une case actuelle, on ajoute la case actuelle au chemin final et on prend son prédécesseur. 
            while caseActuelle:
                cheminFinal.append(caseActuelle)
                caseActuelle = caseActuelle.get_predecesseur()
            
            return cheminFinal, chemin  # TODO mettre listeFerme

        # Suppression de la première case de la liste ouverte.
        listeOuverte.pop(0)

        # Mise à jour de la liste d'adjacence
        listeAdjacente = majListeAdjacente(caseActuelle, [], Plateau)

        # On parcours la liste d'adjacence
        for adjacent in listeAdjacente:
            if adjacent not in listeFerme:

                # Si la case n'est pas dans la liste fermée on calcule son g grâce au g de son "prédecesseur".
                nouveau_g = caseActuelle.get_g() + 1        # TODO a bouger


                if adjacent not in listeOuverte :

                    # Si la case n'est pas dans la liste ouverte, on calcule l'heuristique et f, et on modifie le prédecesseur
                    
                    # TODO revoir l'ordre 
                    adjacent.set_g(nouveau_g)       
                    adjacent.calcul_heuristique(caseFin, heuristique)
                    adjacent.calcul_f()
                    adjacent.set_predecesseur(caseActuelle)

                    if adjacent not in listeOuverte:    # TODO A enlever
                        listeOuverte.append(adjacent)
    return [], []   # On retourne deux tableaux vides, si aucune solution n'est trouvée.