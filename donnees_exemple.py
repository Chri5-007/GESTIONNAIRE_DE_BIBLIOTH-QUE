"""Remplit la base BiblioIIT Lite avec des données fictives de démonstration.

Usage : python donnees_exemple.py
Crée plus de 50 livres, 50 lecteurs et 50 prêts (historique, en cours, en retard).
À lancer une seule fois : le script s'arrête si la base contient déjà des données.
"""
import random
import sys
import unicodedata
from datetime import timedelta

import config
import utils
from database.connexion import initialiser_base, obtenir_connexion
from models.lecteur import Lecteur
from models.livre import Livre
from models.pret import Pret
from repositories.lecteur_repository import LecteurRepository
from repositories.livre_repository import LivreRepository
from repositories.pret_repository import PretRepository

# (titre, auteur, catégorie)
LIVRES = [
    ("L'Étranger", "Albert Camus", "Roman"),
    ("La Peste", "Albert Camus", "Roman"),
    ("Le Petit Prince", "Antoine de Saint-Exupéry", "Roman"),
    ("Les Misérables", "Victor Hugo", "Roman"),
    ("Notre-Dame de Paris", "Victor Hugo", "Roman"),
    ("Germinal", "Émile Zola", "Roman"),
    ("Une si longue lettre", "Mariama Bâ", "Roman"),
    ("Le Père Goriot", "Honoré de Balzac", "Roman"),
    ("Madame Bovary", "Gustave Flaubert", "Roman"),
    ("Le Rouge et le Noir", "Stendhal", "Roman"),
    ("Candide", "Voltaire", "Roman"),
    ("Bel-Ami", "Guy de Maupassant", "Roman"),
    ("Le Comte de Monte-Cristo", "Alexandre Dumas", "Roman"),
    ("Les Trois Mousquetaires", "Alexandre Dumas", "Roman"),
    ("Voyage au bout de la nuit", "Louis-Ferdinand Céline", "Roman"),
    ("La Nausée", "Jean-Paul Sartre", "Roman"),
    ("L'Aventure ambiguë", "Cheikh Hamidou Kane", "Roman"),
    ("Les Soleils des indépendances", "Ahmadou Kourouma", "Roman"),
    ("Allah n'est pas obligé", "Ahmadou Kourouma", "Roman"),
    ("Le Vieux Nègre et la médaille", "Ferdinand Oyono", "Roman"),
    ("L'Enfant noir", "Camara Laye", "Roman"),
    ("Le Monde s'effondre", "Chinua Achebe", "Roman"),
    ("Les Fleurs du mal", "Charles Baudelaire", "Poésie"),
    ("Cahier d'un retour au pays natal", "Aimé Césaire", "Poésie"),
    ("Huis clos", "Jean-Paul Sartre", "Théâtre"),
    ("Le Cid", "Pierre Corneille", "Théâtre"),
    ("Tartuffe", "Molière", "Théâtre"),
    ("Antigone", "Jean Anouilh", "Théâtre"),
    ("Introduction aux algorithmes", "Thomas H. Cormen", "Informatique"),
    ("Python pour les nuls", "John Paul Mueller", "Informatique"),
    ("Clean Code", "Robert C. Martin", "Informatique"),
    ("Design Patterns", "Erich Gamma", "Informatique"),
    ("The Pragmatic Programmer", "Andrew Hunt", "Informatique"),
    ("Le langage C", "Brian W. Kernighan", "Informatique"),
    ("Systèmes d'exploitation", "Andrew Tanenbaum", "Informatique"),
    ("Réseaux", "Andrew Tanenbaum", "Informatique"),
    ("Database System Concepts", "Abraham Silberschatz", "Informatique"),
    ("Intelligence artificielle", "Stuart Russell", "Informatique"),
    ("Compilateurs", "Alfred Aho", "Informatique"),
    ("Algèbre linéaire", "Gilbert Strang", "Mathématiques"),
    ("Principles of Mathematical Analysis", "Walter Rudin", "Mathématiques"),
    ("Calculus", "Michael Spivak", "Mathématiques"),
    ("Algèbre", "Serge Lang", "Mathématiques"),
    ("Graph Theory", "Reinhard Diestel", "Mathématiques"),
    ("Une brève histoire du temps", "Stephen Hawking", "Sciences"),
    ("L'Origine des espèces", "Charles Darwin", "Sciences"),
    ("Sapiens", "Yuval Noah Harari", "Histoire"),
    ("Histoire de l'Afrique noire", "Joseph Ki-Zerbo", "Histoire"),
    ("Le Contrat social", "Jean-Jacques Rousseau", "Philosophie"),
    ("Discours de la méthode", "René Descartes", "Philosophie"),
    ("De l'esprit des lois", "Montesquieu", "Philosophie"),
    ("Principes de l'économie", "N. Gregory Mankiw", "Économie"),
    ("Le Capital", "Karl Marx", "Économie"),
    ("Le Horla", "Guy de Maupassant", "Roman"),
    ("La Condition humaine", "André Malraux", "Roman"),
    ("Le Grand Meaulnes", "Alain-Fournier", "Roman"),
    ("Thérèse Raquin", "Émile Zola", "Roman"),
    ("Le Ventre de Paris", "Émile Zola", "Roman"),
]

PRENOMS = [
    "Aminata", "Moussa", "Fatou", "Ibrahim", "Salimata", "Abdoulaye", "Mariam", "Seydou", "Awa",
    "Mamadou", "Kadiatou", "Oumar", "Rokia", "Sékou", "Nafissatou", "Boubacar", "Djénéba",
    "Lassana", "Hawa", "Yacouba", "Aïcha", "Souleymane", "Bintou", "Adama", "Safiatou",
]
NOMS = [
    "Diallo", "Traoré", "Koné", "Ouattara", "Bamba", "Camara", "Keïta", "Sylla", "Coulibaly",
    "Sow", "Barry", "Cissé", "Fofana", "Touré", "Doumbia", "Sangaré", "Diarra", "Konaté",
    "Sidibé", "Sanogo",
]

NB_LECTEURS = 55
NB_PRETS_EN_COURS = 22
NB_PRETS_EN_RETARD = 10
NB_PRETS_HISTORIQUE = 33


def sans_accents(texte: str) -> str:
    return unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().lower()


def main():
    random.seed(2026)
    conn = obtenir_connexion()
    initialiser_base(conn)
    livres = LivreRepository(conn)
    lecteurs = LecteurRepository(conn)
    prets = PretRepository(conn)

    if livres.lister() or lecteurs.lister():
        print("La base contient déjà des données : aucune donnée ajoutée.")
        conn.close()
        sys.exit(1)

    # --- Livres ---
    quantites = {}
    for titre, auteur, categorie in LIVRES:
        quantite = random.randint(1, 4)
        livre_id = livres.ajouter(Livre(titre, auteur, "", categorie, quantite))
        quantites[livre_id] = quantite

    # --- Lecteurs ---
    combinaisons = [(p, n) for p in PRENOMS for n in NOMS]
    random.shuffle(combinaisons)
    aujourdhui = utils.aujourdhui()
    lecteur_ids = []
    for i, (prenom, nom) in enumerate(combinaisons[:NB_LECTEURS], start=1):
        contact = f"{sans_accents(prenom)}.{sans_accents(nom)}@example.com"
        lecteur_ids.append(lecteurs.ajouter(Lecteur(f"C{i:03d}", nom, prenom, contact)))

    # --- Prêts ---
    emprunts_livre = {lid: 0 for lid in quantites}
    emprunts_lecteur = {lid: 0 for lid in lecteur_ids}
    paires = set()

    def tirer_paire():
        while True:
            livre_id = random.choice(list(quantites))
            lecteur_id = random.choice(lecteur_ids)
            if (
                emprunts_livre[livre_id] < quantites[livre_id]
                and emprunts_lecteur[lecteur_id] < config.NB_MAX_LIVRES_PAR_LECTEUR
                and (livre_id, lecteur_id) not in paires
            ):
                paires.add((livre_id, lecteur_id))
                emprunts_livre[livre_id] += 1
                emprunts_lecteur[lecteur_id] += 1
                return livre_id, lecteur_id

    duree = config.DUREE_PRET_JOURS
    for _ in range(NB_PRETS_EN_COURS):  # prêts récents, dans les délais
        livre_id, lecteur_id = tirer_paire()
        debut = aujourdhui - timedelta(days=random.randint(0, duree - 1))
        prets.ajouter(Pret(livre_id, lecteur_id, utils.vers_iso(debut),
                           utils.vers_iso(debut + timedelta(days=duree))))

    for _ in range(NB_PRETS_EN_RETARD):  # prêts non rendus, échéance dépassée
        livre_id, lecteur_id = tirer_paire()
        debut = aujourdhui - timedelta(days=duree + random.randint(2, 20))
        prets.ajouter(Pret(livre_id, lecteur_id, utils.vers_iso(debut),
                           utils.vers_iso(debut + timedelta(days=duree))))

    for _ in range(NB_PRETS_HISTORIQUE):  # prêts déjà rendus
        livre_id = random.choice(list(quantites))
        lecteur_id = random.choice(lecteur_ids)
        debut = aujourdhui - timedelta(days=random.randint(30, 150))
        prevue = debut + timedelta(days=duree)
        retour = debut + timedelta(days=random.randint(3, duree + 6))
        pret_id = prets.ajouter(Pret(livre_id, lecteur_id, utils.vers_iso(debut), utils.vers_iso(prevue)))
        prets.enregistrer_retour(pret_id, utils.vers_iso(retour))

    conn.close()
    total = NB_PRETS_EN_COURS + NB_PRETS_EN_RETARD + NB_PRETS_HISTORIQUE
    print(f"{len(LIVRES)} livres, {NB_LECTEURS} lecteurs et {total} prêts ajoutés "
          f"({NB_PRETS_EN_COURS} en cours, {NB_PRETS_EN_RETARD} en retard, {NB_PRETS_HISTORIQUE} rendus).")


if __name__ == "__main__":
    main()
