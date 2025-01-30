from FileReader import FileReader
from Plateau import Plateau, genererPlateau

if __name__ == "__main__":
    # Read and analyze the file
    file_reader = FileReader("test.txt")
    characters, total_lines, max_columns = file_reader.analyze_characters()

    # Create a Plateau object
    plateau = Plateau(total_lines, max_columns, characters)

    # Print the attributes of the Plateau object
    print(f"Longueur: {plateau.longueur}")
    print(f"Largeur: {plateau.largeur}")
    print("Liste des cases:")
    for case in plateau.getListeCases():
        print(case)




def ecriture_plateeu(chemin_fichier, chaine_a_ecrire, nbCol):
    """
    Ecrit la chaîne de caractères dans un fichier texte.
    Chaque ligne du fichier contient au maximum nbCol caractères.

    :param chemin_fichier: Chemin du fichier où écrire la chaîne.
    :param chaine_a_ecrire: Chaîne de caractères à écrire.
    """
    # Decoupe la chaine en morceaux de taille nbCol
    morceaux = [chaine_a_ecrire[i:i + nbCol] for i in range(0, len(chaine_a_ecrire), nbCol)]

    # Ecrit chaque morceau dans le fichier
    with open(chemin_fichier, 'w', encoding='utf-8') as file:
        for morceau in morceaux:
            file.write(morceau + '\n')
# chaine = "XXXXXXOOOOOO"
chaine = genererPlateau(5, 5, 30, False)

chemin = "C:\\Users\\adris\\Documents\\000-Cours\\000-SAE-Aetoile\\output.txt"
nbCol = 3
ecriture_plateeu(chemin, chaine, nbCol)
