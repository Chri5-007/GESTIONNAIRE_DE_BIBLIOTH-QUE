from models.livre import Livre

_SELECT = """
SELECT l.*, l.quantite - (
    SELECT COUNT(*) FROM pret p WHERE p.livre_id = l.id AND p.date_retour_reelle IS NULL
) AS disponibles
FROM livre l
"""


class LivreRepository:
    def __init__(self, conn):
        self.conn = conn

    def ajouter(self, livre: Livre) -> int:
        cur = self.conn.execute(
            "INSERT INTO livre (titre, auteur, isbn, categorie, quantite) VALUES (?, ?, ?, ?, ?)",
            (livre.titre, livre.auteur, livre.isbn, livre.categorie, livre.quantite),
        )
        self.conn.commit()
        return cur.lastrowid

    def supprimer(self, livre_id: int):
        self.conn.execute("DELETE FROM livre WHERE id=?", (livre_id,))
        self.conn.commit()

    def trouver(self, livre_id: int):
        r = self.conn.execute(_SELECT + " WHERE l.id=?", (livre_id,)).fetchone()
        return dict(r) if r else None

    def lister(self):
        rows = self.conn.execute(_SELECT + " ORDER BY l.titre").fetchall()
        return [dict(r) for r in rows]

    def rechercher(self, terme: str):
        motif = f"%{terme}%"
        rows = self.conn.execute(
            _SELECT + " WHERE l.titre LIKE ? OR l.auteur LIKE ? OR l.isbn LIKE ? OR l.categorie LIKE ? "
            "ORDER BY l.titre",
            (motif, motif, motif, motif),
        ).fetchall()
        return [dict(r) for r in rows]
