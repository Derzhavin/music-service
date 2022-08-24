from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.Database import (
    get_db_connection,
)
from app.models.domain.MusicTrackModel import MusicTrackModel


class MusicTrackRepository:
    db: Session

    def __init__(self, db: Session = Depends(get_db_connection)):
        self.db = db

    def get(self, skip: int = 0, limit: int = 5):
        query = self.db.query(MusicTrackModel)
        total = query.count()
        items = query.limit(limit).offset(skip).all()

        return items, total
