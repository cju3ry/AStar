from Case import Case
import random
class Plateau:
    def __init__(self, longueur, largeur, listeCases):
        self.longueur = longueur
        self.largeur = largeur
        total = self.longueur * self.largeur

        if (len(listeCases)) != total :
            raise ValueError("Le nombre de cases ne correspond pas à la taille du plateau")

        for case in listeCases :
            if (case.get_x() > self.longueur or case.get_y() > self.largeur) :
                raise ValueError("Les coordonnées de la case ne sont pas dans le plateau")
        
        self.listeCases = listeCases

    def getListeCases(self) :
        return self.listeCases

def genererPlateau(longueur, largeur, tauxDeMur, departArriveeOk: bool):
    if longueur < 3 or largeur < 3 or type(longueur) != int or type(largeur) != int:
        raise ValueError("La longueur et la largeur doivent être supérieures ou égales à 3")

    if longueur is None and largeur is None:
        longueur = random.randint(3, 20)
        largeur = random.randint(3, 20)

    taillePlateau = longueur * largeur

    if not departArriveeOk:
        emplacementDepart = random.randint(0, taillePlateau - 1)
        emplacementArrivee = random.randint(0, taillePlateau - 1)

    chaineEtat = ""
    for i in range(taillePlateau):
        if departArriveeOk and i == 0:
            chaineEtat += 'D'
        elif departArriveeOk and i == taillePlateau - 1:
            chaineEtat += 'A'
        elif not departArriveeOk and i == emplacementDepart:
            chaineEtat += 'D'
        elif not departArriveeOk and i == emplacementArrivee:
            chaineEtat += 'A'
        else:
            generationMur = random.randint(0, 100)
            if generationMur < tauxDeMur:
                chaineEtat += 'X'
            else:
                chaineEtat += 'O'

    return chaineEtat

def ecriture_plateau(chemin_fichier, chaine_a_ecrire, nbCol):
    """
    Écrit la chaîne de caractères dans un fichier texte.
    Chaque ligne du fichier contient exactement `nbCol` caractères.

    :param chemin_fichier: Chemin du fichier où écrire la chaîne.
    :param chaine_a_ecrire: Chaîne de caractères à écrire.
    :param nbCol: Nombre de colonnes par ligne.
    """
    with open(chemin_fichier, 'w', encoding='utf-8') as file:
        for i in range(0, len(chaine_a_ecrire), nbCol):
            file.write(chaine_a_ecrire[i:i + nbCol] + '\n')  # Ajoute un retour à la ligne
