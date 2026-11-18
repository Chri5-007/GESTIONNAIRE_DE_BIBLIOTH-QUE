from datetime import timedelta

import config
import utils
from controllers.base_controller import BaseController
from models.erreurs import ErreurMetier
from models.pret import Pret


class PretController(BaseController):
    def __init__(self, vue, livres, lecteurs, prets):
        super().__init__(vue)
        self.livres = livres
        self.lecteurs = lecteurs
        self.prets = prets
        self.actions = {
            "1": self.emprunter,
            "2": self.retourner,
            "3": self.lister_en_cours,
            "4": self.lister_en_retard,
        }

    def _lecteur(self):
        lecteur = self.lecteurs.trouver_par_carte(self.vue.demander("Numéro de carte du lecteur"))
        if lecteur is None:
            raise ErreurMetier("Lecteur introuvable.")
        return lecteur

    def _livre(self):
        livre = self.livres.trouver(self.vue.demander_entier("ID du livre", minimum=1))
        if livre is None:
            raise ErreurMetier("Livre introuvable.")
        return livre

    def emprunter(self):
        lecteur = self._lecteur()
        livre = self._livre()
        if livre["disponibles"] <= 0:
            raise ErreurMetier("Aucun exemplaire disponible.")
        if self.prets.en_cours(livre["id"], lecteur.id):
            raise ErreurMetier("Ce lecteur a déjà emprunté ce livre.")
        if self.prets.compter_en_cours_lecteur(lecteur.id) >= config.NB_MAX_LIVRES_PAR_LECTEUR:
            raise ErreurMetier(f"Limite atteinte : {config.NB_MAX_LIVRES_PAR_LECTEUR} livres maximum par lecteur.")
        aujourdhui = utils.aujourdhui()
        prevue = aujourdhui + timedelta(days=config.DUREE_PRET_JOURS)
        self.prets.ajouter(Pret(livre["id"], lecteur.id, utils.vers_iso(aujourdhui), utils.vers_iso(prevue)))
        self.vue.succes(
            f"Prêt enregistré : « {livre['titre']} » pour {lecteur.prenom} {lecteur.nom}, "
            f"à rendre le {utils.vers_iso(prevue)}."
        )

    def retourner(self):
        lecteur = self._lecteur()
        livre = self._livre()
        pret = self.prets.en_cours(livre["id"], lecteur.id)
        if pret is None:
            raise ErreurMetier("Aucun prêt en cours de ce livre pour ce lecteur.")
        aujourdhui = utils.aujourdhui()
        self.prets.enregistrer_retour(pret["id"], utils.vers_iso(aujourdhui))
        self.vue.succes("Retour enregistré.")
        retard = (aujourdhui - utils.depuis_iso(pret["date_retour_prevue"])).days
        if retard > 0:
            self.vue.info(f"Attention : retour avec {retard} jour(s) de retard.")

    def lister_en_cours(self):
        self.vue.afficher_prets(self.prets.lister_en_cours())

    def lister_en_retard(self):
        aujourdhui = utils.aujourdhui()
        prets = self.prets.lister_en_retard(utils.vers_iso(aujourdhui))
        for p in prets:
            p["jours_retard"] = (aujourdhui - utils.depuis_iso(p["date_retour_prevue"])).days
        self.vue.afficher_prets(prets, avec_retard=True)
