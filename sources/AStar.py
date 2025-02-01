from Case import Case
from Plateau import Plateau

def trouverFin(listeCase):
    for case in listeCase:
        if case.char == "A":
            caseFin = case
    return caseFin

def trouverDebut(listeCase):
    for case in listeCase:
        if case.char == "D":
            caseDebut = case
    return caseDebut

def majListeAdjacente(caseActuelle, listeAdjacente, Plateau):
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

def choixSuivant(caseActuelle, listeAdjacente, listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin):
    print("=== Début de l'appel ===")
    print(f"Case actuelle: {caseActuelle}")
    print(f"Chemin actuel: {chemin}")

    if len(chemin) == 0:
        chemin.append(caseActuelle)
        print(f"Ajout de la case actuelle au chemin (cas chemin vide): {chemin}")
    else:
        for i, case in enumerate(chemin):
            if case == caseActuelle.get_predecesseur():
                chemin = chemin[:i + 1]
                chemin.append(caseActuelle)
                print(f"Retour en arrière dans le chemin, ajout de {caseActuelle} après {chemin[i]}")
                break
        else:
            chemin.clear()
            chemin.append(caseActuelle)
            print(f"Réinitialisation du chemin, ajout de {caseActuelle}: {chemin}")

    if caseActuelle == caseFin:
        print(f"Arrivée à la case finale: {caseActuelle}")
        print(f"Chemin final: {chemin}")
        return chemin

    print("Mise à jour de la liste des cases adjacentes...")
    listeAdjacente.clear()
    listeAdjacente = majListeAdjacente(caseActuelle, listeAdjacente, Plateau)
    print(f"Liste des cases adjacentes: {listeAdjacente}")

    print("Traitement des cases adjacentes...")
    for adjacent in listeAdjacente:
        if adjacent not in listeFerme:
            print(f"Traitement de l'adjacente: {adjacent}")
            print(f"Calcul de l'heuristique pour {adjacent}")
            adjacent.set_g(len(chemin))  # Vous pouvez aussi calculer g d'une manière plus détaillée selon votre logique
            adjacent.calcul_heuristique(caseFin)
            print(f"Calcul de l'heuristique pour {adjacent}: {adjacent.get_h()}")
            adjacent.calcul_f()
            adjacent.set_predecesseur(caseActuelle)
            if adjacent not in listeOuverte:
                listeOuverte.append(adjacent)
                print(f"Ajout de {adjacent} à la liste ouverte")

    # Trie de la liste ouverte uniquement par f
    print(f"Liste ouverte avant tri: {listeOuverte}")
    listeOuverte.sort(key=lambda case: case.get_f())
    listeOuverte.sort(key=lambda case: case.get_h())
    print(f"Liste ouverte après tri: {listeOuverte}")

    while listeOuverte:
        ouverte = listeOuverte.pop(0)
        print(f"Traitement de la case ouverte: {ouverte}")
        listeFerme.append(ouverte)
        chemin = choixSuivant(ouverte, [], listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin)

        print(f"Chemin après exploration de {ouverte}: {chemin}")
        if chemin:
            print("Chemin trouvé, retour du résultat")
            return chemin

    print("Aucun chemin trouvé")
    return "Aucun chemin"
