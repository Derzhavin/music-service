from app.models.domain.BaseModel import EntityMeta

from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)


class UserModel(EntityMeta):
    __tablename__ = "users"

    id = Column(Integer)
    name = Column(String(50), nullable=False)
    hashed_password = Column(String(256), nullable=False)

    PrimaryKeyConstraint(id)