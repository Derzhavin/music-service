from app.models.domain.BaseModel import EntityMeta

from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)


class MusicTracksFolderModel(EntityMeta):
    __tablename__ = "music_tracks_folders"

    id = Column(Integer)
    PrimaryKeyConstraint(id)
    folder_name = Column(String, nullable=False)