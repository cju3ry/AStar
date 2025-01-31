from Plateau import genererPlateau, ecriture_plateeu

# Generate a random Plateau
chaine = genererPlateau(5, 5, 30, False)
# Define the file path and number of columns
#chemin = "C:\\Users\\adris\\Documents\\000-Cours\\000-SAE-Aetoile\\output.txt"
chemin = "output.txt"
nbCol = 5

# Write the generated Plateau to the file
ecriture_plateeu(chemin, chaine, nbCol)