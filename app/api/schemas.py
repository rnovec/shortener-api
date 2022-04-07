from datetime import datetime

from pydantic import BaseModel, HttpUrl


class Shortener(BaseModel):
    url: HttpUrl


class ShortenerRead(BaseModel):
    id: int
    url: HttpUrl
    code: str
    created_at: datetime

    class Config:
        orm_mode = True
