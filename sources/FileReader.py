from Caractere import Caractere

class FileReader:
    def __init__(self, file_path):
        """Initialise la classe avec le chemin du fichier."""
        self.file_path = file_path

    def analyze_characters(self):
        """
        Lit le contenu du fichier et analyse chaque caractère.
        Retourne une liste d'objets Caractere.
        """
        try:
            characters = []
            with open(self.file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, start=0):  # Numérotation des lignes commence à 0
                    for col_num, char in enumerate(line, start=0):  # Numérotation des colonnes commence à 0
                        if char in {'X', 'O', 'A', 'D'}:
                            characters.append(Caractere(line_num, col_num, char))
                        else:
                            characters.append(Caractere(line_num, col_num, "caractère incorrect"))
            return characters
        except FileNotFoundError:
            return [f"Erreur : Le fichier '{self.file_path}' n'existe pas."]
        except IOError as e:
            return [f"Erreur de lecture : {e}"]
