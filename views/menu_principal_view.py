from views.console import VueBase, choisir


class MenuPrincipalView(VueBase):
    def afficher(self) -> str:
        return choisir(
            "BIBLIOIIT LITE - GESTION DE BIBLIOTHÈQUE",
            [
                ("1", "Livres"),
                ("2", "Lecteurs"),
                ("3", "Prêts et retours"),
                ("9", "Aide : comment utiliser l'application"),
                ("0", "Quitter"),
            ],
        )

    def au_revoir(self):
        self.info("Au revoir.")
