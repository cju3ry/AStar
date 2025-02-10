from Case import Case
from Plateau import Plateau

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


def choixSuivant(caseActuelle, Plateau, listeOuverte, listeFerme, caseFin, chemin, heuristique):

    if caseActuelle not in listeOuverte:
        listeOuverte.append(caseActuelle)

    while listeOuverte:
        listeOuverte.sort(key=lambda case: (case.get_f(), case.get_h()))
        caseActuelle = listeOuverte[0]
        listeFerme.append(caseActuelle)
        if caseActuelle not in chemin:
            chemin.append(caseActuelle)

        if caseActuelle == caseFin:
            cheminFinal = []
            while caseActuelle:
                cheminFinal.append(caseActuelle)
                caseActuelle = caseActuelle.get_predecesseur()

            return cheminFinal, chemin

        listeOuverte.pop(0)
        listeAdjacente = majListeAdjacente(caseActuelle, [], Plateau)

        for adjacent in listeAdjacente:
            if adjacent not in listeFerme:
                nouveau_g = caseActuelle.get_g() + 1

                if adjacent not in listeOuverte :
                    adjacent.set_g(nouveau_g)
                    adjacent.calcul_heuristique(caseFin, heuristique)
                    adjacent.calcul_f()
                    adjacent.set_predecesseur(caseActuelle)

                    if adjacent not in listeOuverte:
                        listeOuverte.append(adjacent)
    return [], []