import livre as Lv


class Biblioteque:
    def __init__(self):
        self.catalogue = []

    def ajouter_livre(self):
        print("\n=== Ajouter un livre ===")
        titre = input("Entrez le titre du livre : ")
        auteur = input("Entrez l'auteur du livre : ")
        annee = input("Entrez l'annee de parution du livre : ")

        nouveau_livre = Lv.Livre(titre, auteur, annee)
        self.catalogue.append(nouveau_livre)
        print(f"Le livre {titre} a ete ajoute a la biblioteque. ")

    def afficher_livre(self):
        print("=== Liste des livres ===")
        if not self.catalogue:
            print("La bibliotheque est vide.")
        else:
            for i, livre in enumerate(self.catalogue, 1):
                print(f"{i}. {livre} - {livre.emprunte}")

    def verifier_livre(self):
        disponible = False
        for livre in self.catalogue:
            if not livre.emprunte:
                return False
        return True

    def afficher_livres_empruntes(self):
        print("=== Livres empruntés ===")
        livres_empruntes = [livre for livre in self.catalogue if livre.emprunte]
        if not livres_empruntes:
            print("Aucun livre emprunté.")
        else:
            for i, livre in enumerate(livres_empruntes, 1):
                print(f"{i}. {livre}")

    def afficher_livres_disponibles(self):
        print("=== Livres disponibles ===")
        livres_disponibles = [livre for livre in self.catalogue if not livre.emprunte]
        if not livres_disponibles:
            print("Aucun livre disponible.")
        else:
            for i, livre in enumerate(livres_disponibles, 1):
                print(f"{i}. {livre}")

    def emprunter_livre(self):
        print("\n=== Emprunter un Livre ===")
        if not self.catalogue:
            print("Aucun livre dans la biblotheque.")
            return

        if self.verifier_livre():
            print("Il n'y a pas de livre a emprunter !")
            return

        self.afficher_livres_disponibles()

        choix = input("Entrez le numéro du livre a emprunter : ")
        try:
            index = int(choix) - 1
            livres_disponibles = [
                livre for livre in self.catalogue if not livre.emprunte
            ]
            if 0 <= index < len(livres_disponibles):
                livre = livres_disponibles[index]
                if livre.emprunte:
                    print("Ce livre est deja emprunte...")
                else:
                    livre.emprunte = True
                    print(f"Vous avez emprunte : {livre.titre}")
            else:
                print("Numéro invalide.")

        except ValueError:
            print("Entre non valide.")

    def rendre_livre(self):
        print("=== Rendre un Livre ===")

        if not self.catalogue:
            print("Aucun livre dans la bibliotheque")
            return

        self.afficher_livres_empruntes()
        livres_empruntes = [livre for livre in self.catalogue if livre.emprunte]
        if not livres_empruntes:
            print("Aucun livre emprunté.")
            return

        choix = input("Entrez le numéro du livre à rendre : ")
        try:
            index = int(choix) - 1
            if 0 <= index < len(livres_empruntes):
                livre = livres_empruntes[index]
                if livre.emprunte:
                    livre.emprunte = False
                    print(f"Vous avez rendu : {livre.titre}")
                else:
                    print("Ce livre n'est pas emprunté.")
            else:
                print("Numéro invalide.")
        except ValueError:
            print("Entrée non valide.")
