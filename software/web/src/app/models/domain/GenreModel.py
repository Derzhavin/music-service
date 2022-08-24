from app.models.domain.BaseModel import EntityMeta

from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)


class GenreModel(EntityMeta):
    __tablename__ = "genres"

    id = Column(Integer)
    PrimaryKeyConstraint(id)
    genre_name = Column(String, nullable=False)