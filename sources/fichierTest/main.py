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





# chaine = "XXXXXXOOOOOO"
#chaine = genererPlateau(5, 5, 30, False)

#chemin = "C:\\Users\\adris\\Documents\\000-Cours\\000-SAE-Aetoile\\output.txt"
#nbCol = 3
#ecriture_plateeu(chemin, chaine, nbCol)
