from sqlalchemy.orm import Session

from ..database import models
from . import schemas, utils


def get_shortener_by_code(db: Session, code: str):
    return db.query(models.Shortener).filter(models.Shortener.code == code).first()


def create_shortener(db: Session, payload: schemas.Shortener):
    code = utils.generate_code()
    shortener = get_shortener_by_code(db, code)
    if shortener is None:
        shortener = models.Shortener(url=payload.url, code=code)
        db.add(shortener)
        db.commit()
        db.refresh(shortener)
    return shortener
