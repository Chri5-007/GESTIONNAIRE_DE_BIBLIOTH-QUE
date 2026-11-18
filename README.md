# BiblioIIT Lite

Version simplifiée de BiblioIIT : application console de gestion de bibliothèque (Python, SQLite, architecture MVC).

## Prise en main rapide (aucune connaissance préalable)

1. **Installer Python 3.8 ou plus récent** depuis https://www.python.org/downloads/ (sous Windows, cocher « Add Python to PATH »).
2. **Décompresser** le dossier `BiblioIIT_Lite`.
3. **Lancer l'application**, dans un terminal ouvert dans le dossier : `python main.py`
4. **Naviguer** : taper le numéro d'une option puis Entrée ; `0` pour revenir en arrière. L'option **9 (Aide)** du menu principal explique tout pas à pas.

La base fournie (`biblioiit_lite.db`) est déjà remplie de **données fictives** : 58 livres, 55 lecteurs et 65 prêts (rendus, en cours et en retard), pour essayer sans risque.

### Essayer en 1 minute

| Je veux... | Je fais... |
|---|---|
| Voir les livres | menu `1` > `2` |
| Chercher un livre | menu `1` > `3` > taper un titre, un auteur ou une catégorie |
| Trouver un lecteur | menu `2` > `3` > taper un nom ou un numéro de carte (ex. `C001`) |
| Prêter un livre | menu `3` > `1` > numéro de carte > ID du livre |
| Enregistrer un retour | menu `3` > `2` > numéro de carte > ID du livre |
| Voir les retards | menu `3` > `4` |

### Repartir d'une base vide ou refaire les données de démonstration

1. Fermer l'application et supprimer le fichier `biblioiit_lite.db`.
2. Pour une base vide : relancer simplement l'application.
3. Pour recréer les données de démonstration : `python donnees_exemple.py`, puis lancer l'application.

## Fonctionnalités

- **Livres** : ajouter, lister, rechercher, supprimer (avec nombre d'exemplaires et disponibilité)
- **Lecteurs** : inscrire, lister, rechercher, supprimer
- **Prêts** : emprunter, retourner, prêts en cours, prêts en retard
- **Aide** intégrée (option 9 du menu principal)

## Paramètres de base

Définis dans `config.py` :

| Paramètre | Valeur |
|---|---|
| Durée d'un prêt | 14 jours |
| Livres max par lecteur | 3 |

## Règles de gestion

- Un prêt est refusé s'il ne reste aucun exemplaire disponible, si le lecteur a déjà ce livre, ou s'il a atteint sa limite.
- Un livre ou un lecteur ayant un historique de prêt ne peut pas être supprimé.
- Un retour tardif affiche un avertissement (pas de suspension dans cette version).

## Architecture

```
BiblioIIT_Lite/
├── main.py              point d'entrée
├── config.py            paramètres de prêt
├── donnees_exemple.py   génère les données de démonstration
├── models/              Livre, Lecteur, Pret
├── views/               menus, aide et affichage console
├── controllers/         livres, lecteurs, prêts
├── repositories/        accès SQLite
├── database/            connexion et création des tables
└── utils.py             fonctions sur les dates
```

## Différences avec la version complète

La version Lite n'a pas : les exemplaires individuels (code d'inventaire, cote, état), les catégories de lecteurs et règles par catégorie, les suspensions après retard, les renouvellements, les réservations et les statistiques.
