import mon_projet.bibliotheque as bibliotheque

while True:
    print("=== Menue Principale ===")
    print("1. Afficher les livres disponibles")
    print("2. Emprunter un livre")
    print("3. Retourner un livre")
    print("4. Ajouter un nouveau livre")
    print("5. Quitter")

    choix = int(input("Choix: "))
    if choix == 1:
        bibliotheque.Biblioteque.ajouter_livre()
    if choix == 5:
        print("Aurevoir !")
        break
