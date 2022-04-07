from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.config import get_session

from . import controllers, schemas

router = APIRouter()


@router.post("/", response_model=schemas.ShortenerRead, status_code=201)
def create_shortener(data: schemas.Shortener, db: Session = Depends(get_session)):
    return controllers.create_shortener(db=db, payload=data)


@router.get("/{shortcode}", response_model=schemas.ShortenerRead)
def retrieve_shortener(shortcode: str, db: Session = Depends(get_session)):
    pass
