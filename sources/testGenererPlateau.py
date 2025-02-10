from Plateau import genererPlateau
from main import ecriture_plateeu

# Generate a random Plateau
chaine = genererPlateau(5, 5, 30, True)

# Define the file path and number of columns
chemin = "C:\\Cours\\projets\\SAE_S4_Math\\Test\\test.txt"
nbCol = 5

# Write the generated Plateau to the file
ecriture_plateeu(chemin, chaine, nbCol)