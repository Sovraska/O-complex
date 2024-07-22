from __future__ import annotations

from sqlalchemy import (Column, String, Integer)
from app.core.config import settings
from app.core.db import Base


class Statistic(Base):
    city_name: str = Column(
        String(length=settings.max_length_string), unique=True, nullable=False
    )
    count: int = Column(Integer)

    def __repr__(self):
        return self.city_name
