from app.models.domain.BaseModel import EntityMeta

from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)


class MusicTrackModel(EntityMeta):
    __tablename__ = "music_tracks"

    id = Column(Integer)
    PrimaryKeyConstraint(id)
    track_name = Column(String(100), nullable=False)
    folder_id = Column(Integer, nullable=False)
    filename = Column(String, nullable=False)

