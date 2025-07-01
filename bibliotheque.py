import livre as Lv


class Biblioteque:
    def __init__(self):
        self.catalogue = []

    def ajouter_livre(self):
        print("\n=== Ajouter un livre ===")
        titre = input("Entrez le titre du livre : ")
        auteur = input("Entrez l'auteur du livre : ")
        annee = input("Entrez l'annee de parution du livre : ")
        isbn = input("Entrez l'ISBN du livre : ")

        nouveau_livre = Lv.Livre(titre, auteur, annee, isbn)
        self.catalogue.append(nouveau_livre)
        print(f"Le livre {titre} a ete ajoute a la biblioteque. ")
