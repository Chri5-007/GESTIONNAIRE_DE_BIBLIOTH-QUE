from models.lecteur import Lecteur


class LecteurRepository:
    def __init__(self, conn):
        self.conn = conn

    @staticmethod
    def _vers_modele(r):
        return Lecteur(
            id=r["id"], numero_carte=r["numero_carte"], nom=r["nom"],
            prenom=r["prenom"], contact=r["contact"] or "",
        )

    def ajouter(self, l: Lecteur) -> int:
        cur = self.conn.execute(
            "INSERT INTO lecteur (numero_carte, nom, prenom, contact) VALUES (?, ?, ?, ?)",
            (l.numero_carte, l.nom, l.prenom, l.contact),
        )
        self.conn.commit()
        return cur.lastrowid

    def supprimer(self, lecteur_id: int):
        self.conn.execute("DELETE FROM lecteur WHERE id=?", (lecteur_id,))
        self.conn.commit()

    def trouver_par_carte(self, numero_carte: str):
        r = self.conn.execute(
            "SELECT * FROM lecteur WHERE numero_carte=?", (numero_carte,)
        ).fetchone()
        return self._vers_modele(r) if r else None

    def lister(self):
        rows = self.conn.execute("SELECT * FROM lecteur ORDER BY nom, prenom").fetchall()
        return [self._vers_modele(r) for r in rows]

    def rechercher(self, terme: str):
        motif = f"%{terme}%"
        rows = self.conn.execute(
            "SELECT * FROM lecteur WHERE nom LIKE ? OR prenom LIKE ? OR numero_carte LIKE ? "
            "ORDER BY nom, prenom",
            (motif, motif, motif),
        ).fetchall()
        return [self._vers_modele(r) for r in rows]
