from controllers.base_controller import BaseController
from models.erreurs import ErreurMetier
from models.livre import Livre


class LivreController(BaseController):
    def __init__(self, vue, livres, prets):
        super().__init__(vue)
        self.livres = livres
        self.prets = prets
        self.actions = {
            "1": self.ajouter,
            "2": self.lister,
            "3": self.rechercher,
            "4": self.supprimer,
        }

    def ajouter(self):
        livre = Livre(**self.vue.saisir_livre())
        livre_id = self.livres.ajouter(livre)
        self.vue.succes(f"Livre ajouté (ID {livre_id}).")

    def lister(self):
        self.vue.afficher_livres(self.livres.lister())

    def rechercher(self):
        terme = self.vue.demander("Recherche (titre, auteur, ISBN ou catégorie)")
        self.vue.afficher_livres(self.livres.rechercher(terme))

    def supprimer(self):
        livre = self.livres.trouver(self.vue.demander_entier("ID du livre", minimum=1))
        if livre is None:
            raise ErreurMetier("Livre introuvable.")
        if self.prets.compter_par_livre(livre["id"]) > 0:
            raise ErreurMetier("Ce livre a un historique de prêt : suppression impossible.")
        if self.vue.confirmer(f"Supprimer « {livre['titre']} » ?"):
            self.livres.supprimer(livre["id"])
            self.vue.succes("Livre supprimé.")
