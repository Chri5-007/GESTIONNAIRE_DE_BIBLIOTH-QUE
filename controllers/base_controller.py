from models.erreurs import ErreurMetier


class BaseController:
    """Boucle de menu commune : la vue affiche le menu, le contrôleur exécute l'action."""

    def __init__(self, vue):
        self.vue = vue
        self.actions = {}

    def executer(self):
        while True:
            choix = self.vue.menu()
            if choix == "0":
                return
            action = self.actions.get(choix)
            if action is None:
                self.vue.erreur("Choix invalide.")
                continue
            try:
                action()
            except ErreurMetier as e:
                self.vue.erreur(str(e))
            self.vue.pause()
