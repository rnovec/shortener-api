from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Shortener(BaseModel):
    url: HttpUrl


class ShortenerReadOnly(Shortener):
    id: int
    shortcode: str
    created_at: datetime

    class Config:
        orm_mode = True
