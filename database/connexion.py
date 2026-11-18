import os
import sqlite3

CHEMIN_BASE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "biblioiit_lite.db"
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS livre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    isbn TEXT,
    categorie TEXT,
    quantite INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE IF NOT EXISTS lecteur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero_carte TEXT NOT NULL UNIQUE,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    contact TEXT
);

CREATE TABLE IF NOT EXISTS pret (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    livre_id INTEGER NOT NULL REFERENCES livre(id),
    lecteur_id INTEGER NOT NULL REFERENCES lecteur(id),
    date_pret TEXT NOT NULL,
    date_retour_prevue TEXT NOT NULL,
    date_retour_reelle TEXT
);
"""


def obtenir_connexion(chemin=CHEMIN_BASE):
    conn = sqlite3.connect(chemin)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialiser_base(conn):
    conn.executescript(SCHEMA)
    conn.commit()
