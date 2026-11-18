BiblioIIT Lite

Application console de gestion de bibliothèque : livres, lecteurs, prêts et retours.
Écrite en Python avec SQLite, sans aucune dépendance externe.

Sommaire
Lancer l’application
Utiliser l’application
Exemples pas à pas
Règles de gestion
Messages d’erreur courants
Repartir de zéro ou refaire la démo
Structure du projet

1. Lancer l’application

Prérequis : Python 3.12 ou plus récent, téléchargeable sur python.org/downloads. Sous Windows, cochez « Add Python to PATH » pendant l’installation.

Vérifiez l’installation :

bash
python --version # Windows
python3 --version # Linux / macOS

Lancez l’application depuis le dossier du projet (celui qui contient main.py) :

bash
python main.py # Windows
python3 main.py # Linux / macOS

La base biblioiit_lite.db est déjà remplie de données fictives : 58 livres, 55 lecteurs et 65 prêts (rendus, en cours et en retard). Vous pouvez essayer sans risque.

2. Utiliser l’application
   Tapez le numéro d’une option, puis Entrée.
   Tapez 0 pour revenir en arrière ou quitter.
   Ctrl+C quitte proprement l’application.
   En cas de saisie incorrecte, un message d’erreur s’affiche : recommencez.
   L’option 9 du menu principal affiche l’aide dans l’application.
   Menu principal
   ============================================================
   BIBLIOIIT LITE - GESTION DE BIBLIOTHÈQUE
   ============================================================
1. Livres
1. Lecteurs
1. Prêts et retours
1. Aide : comment utiliser l'application
1. Quitter
   Les deux identifiants à connaître
   Élément Identifiant Où le trouver
   Livre ID (nombre, ex. 1) Menu 1 > 2 (lister) ou 3 (rechercher)
   Lecteur Numéro de carte (ex. C001) Menu 2 > 2 (lister) ou 3 (rechercher)

Ce sont ces deux identifiants que l’on saisit pour prêter et retourner un livre.

Menus et options
Menu Options

1. Livres 1 Ajouter · 2 Lister · 3 Rechercher (titre, auteur, ISBN, catégorie) · 4 Supprimer
2. Lecteurs 1 Inscrire · 2 Lister · 3 Rechercher (nom, prénom, carte) · 4 Supprimer
3. Prêts et retours 1 Emprunter · 2 Retourner · 3 Prêts en cours · 4 Prêts en retard

Dans la liste des livres, la colonne Total donne le nombre d’exemplaires et la colonne Dispo le nombre d’exemplaires actuellement sur les rayons.

3. Exemples pas à pas
   Prêter un livre
   Menu 1 > 3 : tapez un titre pour trouver l’ID du livre.
   Menu 3 > 1.
   Saisissez le numéro de carte du lecteur (ex. C001), puis l’ID du livre.
   L’application affiche la date de retour prévue.
   Enregistrer un retour
   Menu 3 > 2.
   Saisissez le numéro de carte du lecteur, puis l’ID du livre.
   Si le retour est tardif, un avertissement indique le nombre de jours de retard.
   Voir ce qui est sorti ou en retard
   Prêts en cours : menu 3 > 3
   Prêts en retard (avec les jours de retard) : menu 3 > 4
   Inscrire un lecteur
   Menu 2 > 1.
   Choisissez un numéro de carte unique (ex. C056), puis saisissez le nom, le prénom et un contact (facultatif).
   Ajouter un livre
   Menu 1 > 1.
   Saisissez le titre, l’auteur, l’ISBN et la catégorie (facultatifs), puis le nombre d’exemplaires (1 par défaut).
4. Règles de gestion
   Règle Valeur
   Durée d’un prêt 14 jours
   Livres max par lecteur 3 en même temps
   Un prêt est refusé s’il ne reste aucun exemplaire disponible, si le lecteur a déjà ce livre en cours, ou s’il a atteint sa limite.
   Un livre ou un lecteur ayant un historique de prêt ne peut pas être supprimé.
   Un retour tardif affiche un avertissement, sans suspension dans cette version.

Ces deux valeurs se modifient dans config.py (DUREE_PRET_JOURS, NB_MAX_LIVRES_PAR_LECTEUR).

5. Messages d’erreur courants
   Message Signification Que faire
   Lecteur introuvable. Le numéro de carte n’existe pas Vérifier dans menu 2 > 3
   Livre introuvable. L’ID n’existe pas Vérifier dans menu 1 > 3
   Aucun exemplaire disponible. Tous les exemplaires sont sortis Attendre un retour
   Ce lecteur a déjà emprunté ce livre. Prêt en cours du même livre Enregistrer d’abord le retour
   Limite atteinte : 3 livres maximum par lecteur. Trop de livres empruntés Enregistrer un retour
   Ce numéro de carte existe déjà. Carte déjà attribuée Choisir un autre numéro
   … a un historique de prêt : suppression impossible. Le livre ou le lecteur a déjà servi Rien : l’historique est conservé
   Aucun prêt en cours de ce livre pour ce lecteur. Retour sans prêt correspondant Vérifier le lecteur et l’ID dans les prêts en cours
6. Repartir de zéro ou refaire la démo
   Base vide
   Fermez l’application.
   Supprimez le fichier biblioiit_lite.db.
   Relancez python main.py : une base vide est recréée.
   Retrouver les données de démonstration
   Supprimez biblioiit_lite.db.
   Lancez python donnees_exemple.py.
   Lancez l’application.

Le script de démonstration s’arrête si la base contient déjà des données.

7. Structure du projet
   BiblioIIT_Lite/
   ├── main.py point d'entrée
   ├── config.py paramètres de prêt
   ├── donnees_exemple.py génère les données de démonstration
   ├── models/ Livre, Lecteur, Pret
   ├── views/ menus, aide et affichage console
   ├── controllers/ livres, lecteurs, prêts
   ├── repositories/ accès SQLite
   ├── database/ connexion et création des tables
   └── utils.py fonctions sur les dates

Architecture MVC : les vues affichent, les contrôleurs appliquent les règles, les repositories parlent à SQLite.
