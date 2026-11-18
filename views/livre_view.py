from views.console import VueBase, choisir, tableau


class LivreView(VueBase):
    def menu(self) -> str:
        return choisir(
            "LIVRES",
            [("1", "Ajouter un livre"), ("2", "Lister les livres"),
             ("3", "Rechercher un livre"), ("4", "Supprimer un livre"), ("0", "Retour")],
        )

    def saisir_livre(self) -> dict:
        return {
            "titre": self.demander("Titre"),
            "auteur": self.demander("Auteur"),
            "isbn": self.demander("ISBN", obligatoire=False),
            "categorie": self.demander("Catégorie", obligatoire=False),
            "quantite": self.demander_entier("Nombre d'exemplaires", minimum=1, defaut=1),
        }

    def afficher_livres(self, livres):
        tableau([("ID", "id"), ("Titre", "titre"), ("Auteur", "auteur"), ("ISBN", "isbn"),
                 ("Catégorie", "categorie"), ("Total", "quantite"), ("Dispo", "disponibles")], livres)
