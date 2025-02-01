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
    if len(chemin) == 0:
        chemin.append(caseActuelle)
    else:
        for i, case in enumerate(chemin):
            if case == caseActuelle.get_predecesseur():
                chemin = chemin[:i + 1]
                chemin.append(caseActuelle)
                break
        else:
            chemin.clear()
            chemin.append(caseActuelle)

    if caseActuelle == caseFin:
        return chemin

    listeAdjacente.clear()
    listeAdjacente = majListeAdjacente(caseActuelle, listeAdjacente, Plateau)

    for adjacent in listeAdjacente:
        if adjacent not in listeFerme:
            adjacent.set_g(len(chemin))
            adjacent.calcul_heuristique(caseFin)
            adjacent.calcul_f()
            adjacent.set_predecesseur(caseActuelle)
            if adjacent not in listeOuverte:
                listeOuverte.append(adjacent)

    listeOuverte.sort(key=lambda case: case.get_f())

    while listeOuverte:
        ouverte = listeOuverte.pop(0)
        listeFerme.append(ouverte)
        chemin = choixSuivant(ouverte, [], listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin)
        if chemin:
            return chemin

    return "Auncun chemin "




