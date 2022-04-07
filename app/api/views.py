from fastapi import APIRouter

from .schemas import Shortener, ShortenerReadOnly

router = APIRouter()


@router.post("/", response_model=Shortener)
def create_shortener(url: str):
    pass


@router.get("/{shortcode}", response_model=ShortenerReadOnly)
def retrieve_shortener(shortcode: str):
    pass
