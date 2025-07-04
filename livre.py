class Livre:
    def __init__(
        self,
        titre,
        auteur,
        annee,
    ):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.emprunte = False

    def __str__(self):
        statut = "emprunte" if self.emprunte else "disponible"
        return f"{self.titre}, {self.auteur} ({self.annee})"
