from dataclasses import dataclass
from typing import Optional


@dataclass
class Pret:
    livre_id: int
    lecteur_id: int
    date_pret: str
    date_retour_prevue: str
    date_retour_reelle: Optional[str] = None
    id: Optional[int] = None
