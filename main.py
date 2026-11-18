from controllers.lecteur_controller import LecteurController
from controllers.livre_controller import LivreController
from controllers.pret_controller import PretController
from database.connexion import initialiser_base, obtenir_connexion
from repositories.lecteur_repository import LecteurRepository
from repositories.livre_repository import LivreRepository
from repositories.pret_repository import PretRepository
from views.aide_view import AideView
from views.lecteur_view import LecteurView
from views.livre_view import LivreView
from views.menu_principal_view import MenuPrincipalView
from views.pret_view import PretView


def main(chemin_base=None):
    conn = obtenir_connexion(chemin_base) if chemin_base else obtenir_connexion()
    initialiser_base(conn)

    livres = LivreRepository(conn)
    lecteurs = LecteurRepository(conn)
    prets = PretRepository(conn)

    controleurs = {
        "1": LivreController(LivreView(), livres, prets),
        "2": LecteurController(LecteurView(), lecteurs, prets),
        "3": PretController(PretView(), livres, lecteurs, prets),
    }

    vue = MenuPrincipalView()
    aide = AideView()
    try:
        while True:
            choix = vue.afficher()
            if choix == "0":
                vue.au_revoir()
                break
            if choix == "9":
                aide.afficher()
                continue
            controleur = controleurs.get(choix)
            if controleur is None:
                vue.erreur("Choix invalide.")
                continue
            controleur.executer()
    except (KeyboardInterrupt, EOFError):
        print()
        vue.au_revoir()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
