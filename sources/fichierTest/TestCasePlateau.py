import unittest
import os
import sys

# Add the sources directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sources.Plateau import Plateau, genererPlateau, ecriture_plateau
from sources.Case import Case

class TestCasePlateau(unittest.TestCase):

    def test_initialisation_valide(self):
        """Test si la création de la case fonctionne correctement avec des valeurs valides"""
        case = Case(1, 1, "O")
        self.assertEqual(case.get_x(), 1)
        self.assertEqual(case.get_y(), 1)
        self.assertEqual(case.char, "O")
        self.assertEqual(case.g, 0)
        self.assertEqual(case.h, 0)
        self.assertEqual(case.f, 0)

    def test_initialisation_erreur_coordonnees_negatives(self):
        """Test si une erreur est levée lorsque les coordonnées sont négatives"""
        with self.assertRaises(ValueError) as context:
            Case(-1, 1, "O")
        self.assertEqual(str(context.exception), "Les valeurs des coordonnées (x et y) ne doivent pas être négatives !")

        with self.assertRaises(ValueError) as context:
            Case(1, -1, "O")
        self.assertEqual(str(context.exception), "Les valeurs des coordonnées (x et y) ne doivent pas être négatives !")

    def test_initialisation_erreur_charactere_invalide(self):
        """Test si une erreur est levée lorsque le caractère est invalide"""
        with self.assertRaises(ValueError) as context:
            Case(1, 1, "Z")
        self.assertEqual(str(context.exception), "Caractère non conforme : Z. Attendu : 'O', 'X', 'D' ou 'A'.")

    def test_calcul_heuristique(self):
        """Test si le calcul de l'heuristique fonctionne correctement"""
        start = Case(0, 0, "D")
        end = Case(3, 4, "A")
        start.calcul_heuristique(end)
        self.assertEqual(start.h, 7)  # |0-3| + |0-4| = 3 + 4 = 7

    def test_calcul_f(self):
        """Test si le calcul du coût f fonctionne correctement"""
        case = Case(1, 1, "O")
        case.set_g(5)  # Définit g à 5 et calcule f avec g = 5 et h = 0 (initialement)
        case.calcul_heuristique(Case(3, 3, "A"))  # Calcule l'heuristique, h = 4
        case.calcul_f()  # Re-calculer f en fonction de g et h
        self.assertEqual(case.f, 9)  # f = g + h = 5 + 4 = 9

    def test_set_g(self):
        """Test si la méthode set_g met correctement à jour g et f"""
        case = Case(2, 2, "O")
        case.set_g(8)
        self.assertEqual(case.g, 8)
        case.calcul_heuristique(Case(5, 5, "A"))
        case.calcul_f()
        self.assertEqual(case.f, 14)  # f = g + h (h = |2-5| + |2-5| = 6, donc f = 8 + 6 = 14)

    def test_repr(self):
        """Test si la représentation de la case est correcte"""
        case = Case(2, 3, "X")
        repr_case = repr(case)
        self.assertIn("x=2", repr_case)
        self.assertIn("y=3", repr_case)
        self.assertIn("char=X", repr_case)
        self.assertIn("g=0", repr_case)
        self.assertIn("h=0", repr_case)
        self.assertIn("f=0", repr_case)

    def setUp(self):
        """Initialisation avant chaque test"""
        self.cases = [Case(x, y, "O") for x in range(3) for y in range(3)]
        self.plateau = Plateau(3, 3, self.cases)

    def test_generer_plateau_dimensions_invalides(self):
        """Test si une erreur est levée pour une longueur ou une largeur < 3"""
        with self.assertRaises(ValueError) as context:
            genererPlateau(2, 5, 30, True)  # Longueur invalide
        self.assertEqual(str(context.exception), "La longueur et la largeur doivent être supérieures ou égales à 3")

        with self.assertRaises(ValueError) as context:
            genererPlateau(5, 2, 30, True)  # Largeur invalide
        self.assertEqual(str(context.exception), "La longueur et la largeur doivent être supérieures ou égales à 3")

        with self.assertRaises(ValueError) as context:
            genererPlateau(2, 2, 30, True)  # Longueur et largeur invalides
        self.assertEqual(str(context.exception), "La longueur et la largeur doivent être supérieures ou égales à 3")

    def test_initialisation_correcte(self):
        """Test si le plateau est bien initialisé avec les bonnes dimensions et cases"""
        self.assertEqual(self.plateau.longueur, 3)
        self.assertEqual(self.plateau.largeur, 3)
        self.assertEqual(len(self.plateau.getListeCases()), 9)
        self.assertIsInstance(self.plateau.getListeCases()[0], Case)

    def test_initialisation_erreur_taille(self):
        """Test si une erreur est levée quand la liste de cases ne correspond pas à la taille"""
        cases = [Case(0, 0, "O"), Case(0, 1, "O")]
        with self.assertRaises(ValueError):
            Plateau(3, 3, cases)

    def test_initialisation_erreur_coordonnees(self):
        """Test si une erreur est levée quand une case est hors du plateau"""
        cases = [Case(0, 0, "O"), Case(5, 5, "O")]
        with self.assertRaises(ValueError):
            Plateau(3, 3, cases)

    def test_getListeCases_vide(self):
        """Test si la méthode getListeCases fonctionne avec une liste vide"""
        plateau_vide = Plateau(1, 1, [Case(0, 0, "O")])
        self.assertEqual(len(plateau_vide.getListeCases()), 1)

    def test_generer_plateau_taille(self):
        """Test si la chaîne générée a bien la bonne taille"""
        chaine = genererPlateau(5, 5, 20, True)
        self.assertEqual(len(chaine), 25)

    def test_generer_plateau_depart_arrivee(self):
        """Test si la génération respecte le positionnement du départ et de l'arrivée"""
        chaine = genererPlateau(4, 4, 20, True)
        self.assertEqual(chaine[0], 'D')
        self.assertEqual(chaine[-1], 'A')

    def test_generer_plateau_taux_murs(self):
        """Test si le taux de murs est approximativement respecté"""
        chaine = genererPlateau(10, 10, 50, True)
        nb_murs = chaine.count("X")
        self.assertTrue(40 <= nb_murs <= 60)  # Tolérance de ±10%

    def test_generer_plateau_erreur(self):
        """Test si une erreur est levée avec des dimensions incorrectes"""
        with self.assertRaises(ValueError):
            genererPlateau(2, 2, 30, True)  # Trop petit (minimum 3x3)

    def test_ecriture_plateau(self):
        """Test si le fichier est correctement écrit avec le bon format"""
        fichier_test = "test_plateau.txt"
        chaine = "DXXOXOXOOA"
        nbCol = 5
        ecriture_plateau(fichier_test, chaine, nbCol)

        with open(fichier_test, 'r', encoding='utf-8') as file:
            lignes = file.readlines()


        self.assertEqual(len(lignes), 2)  # Doit créer 2 lignes (10 caractères / 5 colonnes)
        self.assertEqual(lignes[0].strip(), "DXXOX")
        self.assertEqual(lignes[1].strip(), "OXOOA")

        os.remove("test_plateau.txt")   # Enleve le fichier après le test

    def test_ecriture_plateau_fichier_vide(self):
        """Test si l'écriture fonctionne avec une chaîne vide"""
        fichier_test = "test_vide.txt"
        ecriture_plateau(fichier_test, "", 5)

        with open(fichier_test, 'r', encoding='utf-8') as file:
            lignes = file.readlines()

        self.assertEqual(len(lignes), 0)
        os.remove("test_vide.txt")  # Enleve le fichier après le test