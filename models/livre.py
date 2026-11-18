from dataclasses import dataclass
from typing import Optional


@dataclass
class Livre:
    titre: str
    auteur: str
    isbn: str = ""
    categorie: str = ""
    quantite: int = 1
    id: Optional[int] = None
