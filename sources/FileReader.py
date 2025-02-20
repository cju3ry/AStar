from Case import Case

class FileReader:
    def __init__(self, file_path):
        """Initialise la classe avec le chemin du fichier."""
        self.file_path = file_path

    def analyze_characters(self):
        """
        Lit le contenu du fichier et analyse chaque caractère.
        :return: Une liste de caractères, le nombre total de lignes et le nombre maximal de colonnes.
        """
        try:
            characters = []
            max_columns = 0  # Garde la trace du nombre maximal de colonnes
            total_lines = 0  # Garde la trace du nombre total de lignes

            with open(self.file_path, 'r', encoding='utf-8') as file:
                for line_num, line in enumerate(file, start=0):  # Numérotation des lignes commence à 0
                    line = line.rstrip('\n')  # Supprime le saut de ligne à la fin de chaque ligne
                    total_lines += 1
                    max_columns = max(max_columns, len(line))
                    for col_num, char in enumerate(line, start=0):  # Numérotation des colonnes commence à 0
                        # Inversion des coordonnées (x, y) : y pour les lignes, x pour les colonnes
                        characters.append(Case(col_num, line_num, char))  # x = colonne, y = ligne

            print(f"Nombre total de lignes : {total_lines }")
            print(f"Nombre total de colonnes : {max_columns}")
            """Retourne la liste des caractères avec un message"""
            return characters, total_lines, max_columns

        except FileNotFoundError:
            return [f"Erreur : Le fichier '{self.file_path}' n'existe pas."], 0, 0
        except IOError as e:
            return [f"Erreur de lecture : {e}"], 0, 0

def ecriture_plateau(chemin_fichier, chaine_a_ecrire, nbCol):
    """
    Écrit la chaîne de caractères dans un fichier texte.
    Chaque ligne du fichier contient au maximum nbCol caractères.

    Paramètres : 
    chemin_fichier: Chemin du fichier où écrire la chaîne.
    chaine_a_ecrire: Chaîne de caractères à écrire.
    """
    # Découpe la chaîne en morceaux de taille nbCol
    morceaux = [chaine_a_ecrire[i:i + nbCol] for i in range(0, len(chaine_a_ecrire), nbCol)]

    # Ecrit chaque morceau dans le fichier
    with open(chemin_fichier, 'w', encoding='utf-8') as file:
        for morceau in morceaux:
            file.write(morceau + '\n')

def lecture_plateau(chemin_fichier):
    """
    Lit un fichier texte et retourne son contenu sous forme de chaîne de caractères,
    ainsi que le nombre de lignes et le nombre de colonnes.

    Paramètre : 
    chemin_fichier: Chemin du fichier à lire.

    Return : 
    Le contenu du fichier sous forme de chaîne de caractères, le nombre de lignes et le nombre de colonnes.
    """
    with open(chemin_fichier, 'r', encoding='utf-8') as file:
        lignes = file.readlines()

    contenu = ''.join(lignes).replace('\n', '')
    nombre_lignes = len(lignes)
    nombre_colonnes = len(contenu) // nombre_lignes

    return contenu, nombre_lignes, nombre_colonnes
