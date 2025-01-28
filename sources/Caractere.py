class Caractere:
    def __init__(self, ligne, colonne, type_char):
        """
        Initialise un caractère avec sa ligne, sa colonne et son type.
        :param ligne: La ligne où se trouve le caractère (axe Y).
        :param colonne: La colonne où se trouve le caractère (axe X).
        :param type_char: Le type du caractère (A, D, O, X ou caractère incorrect).
        """
        self.ligne = ligne
        self.colonne = colonne
        self.type_char = type_char

    def __str__(self):
        """Retourne une représentation lisible du caractère."""
        return f"Ligne {self.ligne}, Colonne {self.colonne} : {self.type_char}"
