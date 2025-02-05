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

def choixSuivant(caseActuelle, listeAdjacente, listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin, heuristique, caseDepart):
    print("=== Début de l'appel ===")
    print(f"Case actuelle: {caseActuelle}")
    print(f"Chemin actuel: {chemin}")

    cheminFinal = []

    if caseActuelle not in chemin:
        chemin.append(caseActuelle)

    if caseActuelle == caseFin:
        print(f"Arrivée à la case finale: {caseActuelle}")
        print(f"Chemin final: {chemin}")

        while caseActuelle != caseDepart:
            cheminFinal.append(caseActuelle)
            caseActuelle = caseActuelle.get_predecesseur()

        cheminFinal.append(caseDepart)
        cheminFinal.reverse()
        return cheminFinal

    listeAdjacente = majListeAdjacente(caseActuelle, [], Plateau)

    for adjacent in listeAdjacente:
        if adjacent not in listeFerme and adjacent not in listeOuverte:
            adjacent.set_g(len(chemin))
            adjacent.calcul_heuristique(caseFin, heuristique)
            adjacent.calcul_f()
            adjacent.set_predecesseur(caseActuelle)
            listeOuverte.append(adjacent)

    listeOuverte.sort(key=lambda case: (case.get_f(), case.get_h()))

    while listeOuverte:
        ouverte = listeOuverte.pop(0)
        listeFerme.append(ouverte)

        chemin_result = choixSuivant(ouverte, listeAdjacente, listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin[:], heuristique, caseDepart)

        if chemin_result and chemin_result != "Aucun chemin":
            return chemin_result

    return "Aucun chemin"
