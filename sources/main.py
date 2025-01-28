from FileReader import FileReader

if __name__ == "__main__":
    file_reader = FileReader("test.txt")
    resultat = file_reader.analyze_characters()
    for caractere in resultat:
        print(caractere)
