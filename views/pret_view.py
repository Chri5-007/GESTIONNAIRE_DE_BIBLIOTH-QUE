from views.console import VueBase, choisir, tableau


class PretView(VueBase):
    def menu(self) -> str:
        return choisir(
            "PRÊTS ET RETOURS",
            [("1", "Emprunter un livre"), ("2", "Retourner un livre"),
             ("3", "Prêts en cours"), ("4", "Prêts en retard"), ("0", "Retour")],
        )

    def afficher_prets(self, prets, avec_retard: bool = False):
        colonnes = [("ID livre", "livre_id"), ("Titre", "titre"), ("Carte", "numero_carte"),
                    ("Lecteur", "lecteur"), ("Prêté le", "date_pret"), ("À rendre le", "date_retour_prevue")]
        if avec_retard:
            colonnes.append(("Jours de retard", "jours_retard"))
        tableau(colonnes, prets)
