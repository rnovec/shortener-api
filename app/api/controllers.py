from sqlalchemy.orm import Session

from .schemas import Shortener


def get_shortener(db: Session, code: str):
    pass


def create_shortener(db: Session, shortener: Shortener):
    pass
