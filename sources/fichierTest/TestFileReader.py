import unittest
import os
import sys

# Add the sources directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sources.FileReader import FileReader

class TestFileReader(unittest.TestCase):

    def setUp(self):
        """Prépare les fichiers pour les tests."""
        # Crée un fichier de test avec des données
        self.test_file = "test_file.txt"
        self.test_file_empty = "test_empty_file.txt"
        self.test_file_invalid = "non_existent_file.txt"

        # Création d'un fichier de test avec du contenu
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write("DXXOX\nOXOOA\nOOXOX")

        # Création d'un fichier vide pour les tests
        with open(self.test_file_empty, 'w', encoding='utf-8') as f:
            f.write("")

    def tearDown(self):
        """Supprime les fichiers après les tests."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_file_empty):
            os.remove(self.test_file_empty)

    def test_analyze_characters_existing_file(self):
        """Test pour un fichier existant avec des caractères spécifiques"""
        reader = FileReader(self.test_file)
        characters, total_lines, max_columns = reader.analyze_characters()

        # Vérification du nombre total de lignes
        self.assertEqual(total_lines, 3)

        # Vérification du nombre maximal de colonnes
        self.assertEqual(max_columns, 5)

        # Vérification des caractères analysés (on s'attend à ce qu'il y ait 15 cases)
        self.assertEqual(len(characters), 15)

        # Vérification que la première Case est correcte (ligne 0, colonne 0, 'D')
        self.assertEqual(characters[0].get_x(), 0)
        self.assertEqual(characters[0].get_y(), 0)
        self.assertEqual(characters[0].char, 'D')

    def test_analyze_characters_empty_file(self):
        """Test pour un fichier vide"""
        reader = FileReader(self.test_file_empty)
        characters, total_lines, max_columns = reader.analyze_characters()

        # Vérification du nombre total de lignes
        self.assertEqual(total_lines, 0)

        # Vérification du nombre maximal de colonnes
        self.assertEqual(max_columns, 0)

        # Vérification qu'il n'y a pas de caractères
        self.assertEqual(len(characters), 0)

    def test_analyze_characters_file_not_found(self):
        """Test pour un fichier inexistant"""
        reader = FileReader(self.test_file_invalid)
        characters, total_lines, max_columns = reader.analyze_characters()

        # Vérification de l'erreur retournée
        self.assertEqual(characters[0], f"Erreur : Le fichier '{self.test_file_invalid}' n'existe pas.")
        self.assertEqual(total_lines, 0)
        self.assertEqual(max_columns, 0)

    def test_analyze_characters_invalid_file_format(self):
        """Test pour un fichier invalide (contient des erreurs de lecture)"""
        # Crée un fichier temporaire avec un format invalide (par exemple des caractères illisibles)
        invalid_file = "test_invalid_file.txt"
        with open(invalid_file, 'w', encoding='utf-8') as f:
            f.write("DXXO\x80XOXOOA")

        reader = FileReader(invalid_file)

        # Capture l'exception ValueError
        with self.assertRaises(ValueError):
            reader.analyze_characters()

        # Nettoyage du fichier invalide après le test
        os.remove(invalid_file)
