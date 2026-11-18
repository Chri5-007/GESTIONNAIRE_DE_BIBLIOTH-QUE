from dataclasses import dataclass
from typing import Optional


@dataclass
class Lecteur:
    numero_carte: str
    nom: str
    prenom: str
    contact: str = ""
    id: Optional[int] = None
