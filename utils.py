from datetime import date, datetime


def aujourdhui() -> date:
    return date.today()


def vers_iso(d: date) -> str:
    return d.isoformat()


def depuis_iso(texte: str) -> date:
    return datetime.strptime(texte, "%Y-%m-%d").date()
