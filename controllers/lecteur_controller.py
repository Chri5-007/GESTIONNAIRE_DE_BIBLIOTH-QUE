from controllers.base_controller import BaseController
from models.erreurs import ErreurMetier
from models.lecteur import Lecteur


class LecteurController(BaseController):
    def __init__(self, vue, lecteurs, prets):
        super().__init__(vue)
        self.lecteurs = lecteurs
        self.prets = prets
        self.actions = {
            "1": self.inscrire,
            "2": self.lister,
            "3": self.rechercher,
            "4": self.supprimer,
        }

    def inscrire(self):
        donnees = self.vue.saisir_lecteur()
        if self.lecteurs.trouver_par_carte(donnees["numero_carte"]):
            raise ErreurMetier("Ce numéro de carte existe déjà.")
        lecteur = Lecteur(**donnees)
        self.lecteurs.ajouter(lecteur)
        self.vue.succes(f"Lecteur {lecteur.prenom} {lecteur.nom} inscrit (carte {lecteur.numero_carte}).")

    def lister(self):
        self.vue.afficher_lecteurs(self.lecteurs.lister())

    def rechercher(self):
        terme = self.vue.demander("Recherche (nom, prénom ou numéro de carte)")
        self.vue.afficher_lecteurs(self.lecteurs.rechercher(terme))

    def supprimer(self):
        lecteur = self.lecteurs.trouver_par_carte(self.vue.demander("Numéro de carte du lecteur"))
        if lecteur is None:
            raise ErreurMetier("Lecteur introuvable.")
        if self.prets.compter_par_lecteur(lecteur.id) > 0:
            raise ErreurMetier("Ce lecteur a un historique de prêt : suppression impossible.")
        if self.vue.confirmer(f"Supprimer {lecteur.prenom} {lecteur.nom} ?"):
            self.lecteurs.supprimer(lecteur.id)
            self.vue.succes("Lecteur supprimé.")
