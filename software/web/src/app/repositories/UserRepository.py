from fastapi import Depends
from sqlalchemy.orm import Session

from app.configs.Database import (
    get_db_connection,
)
from app.models.domain.UserModel import UserModel


class UserRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def create(self, user: UserModel):
        self.db.add(user)
        self.db.commit()

    def get_user_by_username(self, username: str):
        user = self.db.query(UserModel).filter(UserModel.username == username).first()

        if not user:
            return None
        return user

    def is_username_exists(self, username: str):
        q = self.db.query(UserModel).filter(UserModel.username == username)
        res = self.db.query(q.exists()).scalar()
        return res
