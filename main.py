from bibliotheque import Biblioteque

biblio = Biblioteque()

while True:
    print("=== Menu Principale ===")
    print("1. Ajouter un nouveau livre")
    print("2. Afficher les livres disponibles")
    print("3. Afficher les livres empruntés")
    print("4. Emprunter un livre")
    print("5. Rendre un livre")
    print("6. Quitter")

    choix = int(input("Choix: "))

    if choix == 1:
        biblio.ajouter_livre()
    elif choix == 2:
        biblio.afficher_livres_disponibles()
    elif choix == 3:
        biblio.afficher_livres_empruntes()
    elif choix == 4:
        biblio.emprunter_livre()
    elif choix == 5:
        biblio.rendre_livre()
    elif choix == 6:
        print("Aurevoir !!")
        break
