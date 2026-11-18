from views.console import VueBase, choisir, tableau


class LecteurView(VueBase):
    def menu(self) -> str:
        return choisir(
            "LECTEURS",
            [("1", "Inscrire un lecteur"), ("2", "Lister les lecteurs"),
             ("3", "Rechercher un lecteur"), ("4", "Supprimer un lecteur"), ("0", "Retour")],
        )

    def saisir_lecteur(self) -> dict:
        return {
            "numero_carte": self.demander("Numéro de carte (unique)"),
            "nom": self.demander("Nom"),
            "prenom": self.demander("Prénom"),
            "contact": self.demander("Contact (téléphone ou e-mail)", obligatoire=False),
        }

    def afficher_lecteurs(self, lecteurs):
        tableau([("ID", "id"), ("Carte", "numero_carte"), ("Nom", "nom"),
                 ("Prénom", "prenom"), ("Contact", "contact")],
                [vars(l) for l in lecteurs])
