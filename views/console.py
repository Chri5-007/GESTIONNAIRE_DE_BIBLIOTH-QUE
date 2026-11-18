def titre(texte: str):
    print("\n" + "=" * 60)
    print(f"  {texte}")
    print("=" * 60)


def saisir(message: str, obligatoire: bool = True) -> str:
    while True:
        valeur = input(f"{message} : ").strip()
        if valeur or not obligatoire:
            return valeur
        print("Ce champ est obligatoire.")


def saisir_entier(message: str, minimum=None, defaut=None):
    while True:
        suffixe = f" [{defaut}]" if defaut is not None else ""
        texte = input(f"{message}{suffixe} : ").strip()
        if texte == "" and defaut is not None:
            return defaut
        try:
            valeur = int(texte)
        except ValueError:
            print("Veuillez saisir un nombre entier.")
            continue
        if minimum is not None and valeur < minimum:
            print(f"La valeur doit être au moins {minimum}.")
            continue
        return valeur


def confirmer(message: str) -> bool:
    while True:
        reponse = input(f"{message} (o/n) : ").strip().lower()
        if reponse in ("o", "oui"):
            return True
        if reponse in ("n", "non"):
            return False
        print("Répondez par o ou n.")


def choisir(titre_menu: str, options) -> str:
    titre(titre_menu)
    for code, libelle in options:
        print(f"  {code}. {libelle}")
    return input("\nVotre choix : ").strip()


def tableau(colonnes, lignes):
    """colonnes : liste de (entête, clé). lignes : liste de dict."""
    if not lignes:
        print("\n(aucun résultat)")
        return
    textes = [[str(ligne.get(cle) if ligne.get(cle) is not None else "") for _, cle in colonnes]
              for ligne in lignes]
    largeurs = [max(len(entete), *(len(t[i]) for t in textes)) for i, (entete, _) in enumerate(colonnes)]
    print()
    print(" | ".join(entete.ljust(largeurs[i]) for i, (entete, _) in enumerate(colonnes)))
    print("-+-".join("-" * l for l in largeurs))
    for t in textes:
        print(" | ".join(t[i].ljust(largeurs[i]) for i in range(len(colonnes))))
    print(f"\n{len(lignes)} ligne(s)")


class VueBase:
    def info(self, message: str):
        print(f"\n{message}")

    def succes(self, message: str):
        print(f"\n[OK] {message}")

    def erreur(self, message: str):
        print(f"\n[Erreur] {message}")

    def demander(self, message: str, obligatoire: bool = True) -> str:
        return saisir(message, obligatoire)

    def demander_entier(self, message: str, minimum=None, defaut=None):
        return saisir_entier(message, minimum, defaut)

    def confirmer(self, message: str) -> bool:
        return confirmer(message)

    def pause(self):
        input("\nAppuyez sur Entrée pour continuer...")
