from datetime import datetime

import sqlalchemy as _sql

from .config import Base


class Shortener(Base):
    __tablename__ = "shortener"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    url = _sql.Column(_sql.String(2083), nullable=False)
    code = _sql.Column(_sql.String(4), unique=True, index=True, nullable=False)
    created_at = _sql.Column(_sql.DateTime, default=datetime.utcnow)
