from views.console import VueBase, titre

TEXTE_AIDE = """
COMMENT ÇA MARCHE
  - Tapez le numéro d'une option, puis la touche Entrée.
  - Tapez 0 pour revenir au menu précédent ou pour quitter.
  - Si vous vous trompez de saisie, un message d'erreur s'affiche : recommencez.

LES TROIS RUBRIQUES
  1. Livres         : voir le catalogue, chercher, ajouter, supprimer un livre.
                      Chaque livre a un ID (nombre) : c'est lui qu'on utilise pour les prêts.
                      « Dispo » = exemplaires actuellement présents sur les rayons.
  2. Lecteurs       : inscrire et retrouver les personnes. Chaque lecteur a un numéro de
                      carte (ex. C001) : c'est lui qu'on utilise pour les prêts.
  3. Prêts et retours : enregistrer un emprunt ou un retour, voir ce qui est sorti
                      et ce qui est en retard.

EXEMPLES PAS À PAS
  Prêter un livre :
    menu 3 > option 1 > numéro de carte du lecteur > ID du livre
    (pour trouver l'ID : menu 1 > option 3 « Rechercher un livre »)

  Enregistrer un retour :
    menu 3 > option 2 > numéro de carte du lecteur > ID du livre

  Voir qui est en retard :
    menu 3 > option 4

  Inscrire un nouveau lecteur :
    menu 2 > option 1 > choisissez un numéro de carte unique (ex. C056)

RÈGLES DE PRÊT
  - Un prêt dure 14 jours.
  - Un lecteur peut avoir 3 livres empruntés en même temps.
  - Un livre dont tous les exemplaires sont sortis ne peut plus être emprunté.
  - Un livre ou un lecteur qui a déjà un historique de prêt ne peut pas être supprimé.

LES DONNÉES
  La base contient des données fictives de démonstration (livres, lecteurs, prêts).
  Elles servent à essayer l'application sans risque.
  Pour repartir d'une base vide : fermez l'application, supprimez le fichier
  biblioiit_lite.db, puis relancez-la.
"""


class AideView(VueBase):
    def afficher(self):
        titre("AIDE - COMMENT UTILISER BIBLIOIIT")
        print(TEXTE_AIDE)
        self.pause()
