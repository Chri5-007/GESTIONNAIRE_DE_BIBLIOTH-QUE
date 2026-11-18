from models.pret import Pret

_DETAIL = """
SELECT p.id AS pret_id, li.id AS livre_id, li.titre AS titre,
       le.numero_carte AS numero_carte, le.nom || ' ' || le.prenom AS lecteur,
       p.date_pret AS date_pret, p.date_retour_prevue AS date_retour_prevue
FROM pret p
JOIN livre li ON li.id = p.livre_id
JOIN lecteur le ON le.id = p.lecteur_id
WHERE p.date_retour_reelle IS NULL
"""


class PretRepository:
    def __init__(self, conn):
        self.conn = conn

    def ajouter(self, p: Pret) -> int:
        cur = self.conn.execute(
            "INSERT INTO pret (livre_id, lecteur_id, date_pret, date_retour_prevue) VALUES (?, ?, ?, ?)",
            (p.livre_id, p.lecteur_id, p.date_pret, p.date_retour_prevue),
        )
        self.conn.commit()
        return cur.lastrowid

    def en_cours(self, livre_id: int, lecteur_id: int):
        r = self.conn.execute(
            "SELECT id, date_retour_prevue FROM pret "
            "WHERE livre_id=? AND lecteur_id=? AND date_retour_reelle IS NULL",
            (livre_id, lecteur_id),
        ).fetchone()
        return dict(r) if r else None

    def compter_en_cours_lecteur(self, lecteur_id: int) -> int:
        return self.conn.execute(
            "SELECT COUNT(*) FROM pret WHERE lecteur_id=? AND date_retour_reelle IS NULL",
            (lecteur_id,),
        ).fetchone()[0]

    def compter_par_livre(self, livre_id: int) -> int:
        return self.conn.execute(
            "SELECT COUNT(*) FROM pret WHERE livre_id=?", (livre_id,)
        ).fetchone()[0]

    def compter_par_lecteur(self, lecteur_id: int) -> int:
        return self.conn.execute(
            "SELECT COUNT(*) FROM pret WHERE lecteur_id=?", (lecteur_id,)
        ).fetchone()[0]

    def enregistrer_retour(self, pret_id: int, date_iso: str):
        self.conn.execute("UPDATE pret SET date_retour_reelle=? WHERE id=?", (date_iso, pret_id))
        self.conn.commit()

    def lister_en_cours(self):
        rows = self.conn.execute(_DETAIL + " ORDER BY p.date_retour_prevue").fetchall()
        return [dict(r) for r in rows]

    def lister_en_retard(self, date_iso: str):
        rows = self.conn.execute(
            _DETAIL + " AND p.date_retour_prevue < ? ORDER BY p.date_retour_prevue", (date_iso,)
        ).fetchall()
        return [dict(r) for r in rows]
