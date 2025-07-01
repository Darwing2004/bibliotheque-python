class Livre:
    def __init__(
        self,
        titre,
        auteur,
        annee,
        isbn,
    ):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.ISBN = isbn
        self.disponible = True

    def afficher(self):
        print(f"Titre: {self.titre}")
        print(f"Auteur: {self.auteur}")
        print(f"Année: {self.annee}")
        print(f"ISBN: {self.ISBN}")
        print(f"Disponible: {'Oui' if self.disponible else 'Non'}")
