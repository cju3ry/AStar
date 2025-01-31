from Case import Case
from Plateau import Plateau

def ajoutListeOuverte(caseChoisie, listeOuverte):
    listeOuverte.append(caseChoisie)

def supprimmeListeOuverte(caseChoisie, listeOuverte):
    listeOuverte.remove(caseChoisie)

def majListeFerme(caseUtilisé, listeFerme):
    listeFerme.append(caseUtilisé)


def majListeAdjacente(caseActuelle, listeAdjacente, listeCase):
    xActuel = caseActuelle.get_x()
    yActuel = caseActuelle.get_y()

    if rechercheCase(listeCase, xActuel + 1, yActuel) != 0:



