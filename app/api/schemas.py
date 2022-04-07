from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Shortener(BaseModel):
    url: HttpUrl


class ShortenerRead(Shortener):
    id: int
    code: str
    created_at: datetime

    class Config:
        orm_mode = True
