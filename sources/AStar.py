from Case import Case
from Plateau import Plateau

def trouverFin(listeCase):
    global caseFin
    for case in listeCase:
        if(case.char == "A"):
            caseFin = case

def majListeAdjacente(caseActuelle, listeAdjacente, listeCase, Plateau):
    xActuel = caseActuelle.get_x()
    yActuel = caseActuelle.get_y()

    if Plateau.rechercheCase(listeCase, xActuel + 1, yActuel) != 0:
        listeAdjacente.append(Plateau.rechercheCase(listeCase, xActuel + 1, yActuel))

    if Plateau.rechercheCase(listeCase, xActuel - 1, yActuel) != 0:
        listeAdjacente.append(Plateau.rechercheCase(listeCase, xActuel - 1, yActuel))

    if Plateau.rechercheCase(listeCase, xActuel, yActuel + 1) != 0:
        listeAdjacente.append(Plateau.rechercheCase(listeCase, xActuel + 1, yActuel))

    if Plateau.rechercheCase(listeCase, xActuel, yActuel - 1) != 0:
        listeAdjacente.append(Plateau.rechercheCase(listeCase, xActuel + 1, yActuel))

    return listeAdjacente

def choixSuivant(caseActuelle, listeAdjacente, listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin):

    if len(chemin) == 0 :
        chemin.append(caseActuelle)
    else :
        if caseActuelle.get_predecesseur() != chemin[-1] :
            chemin.clear()
            chemin.append(caseActuelle)
        else:
            chemin.append(caseActuelle)

    if caseActuelle == caseFin:
        return chemin
    listeAdjacente = majListeAdjacente(caseActuelle, listeAdjacente, listeCase, Plateau)
    for adjacent in listeAdjacente:
        if adjacent not in listeFerme:
            adjacent.set_g(len(listeOuverte))
            adjacent.calcul_heuristique(caseFin)
            adjacent.calcul_f()
            adjacent.set_predecesseur(caseActuelle)
            listeOuverte.append(adjacent)
    listeOuverte.sort(key=lambda case: case.get_f())
    for ouverte in listeOuverte :
        listeOuverte.remove(ouverte)
        listeFerme.append(ouverte)
        choixSuivant(ouverte, listeAdjacente, listeCase, Plateau, listeOuverte, listeFerme, caseFin, chemin)



