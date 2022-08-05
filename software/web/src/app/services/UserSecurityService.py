import datetime

from fastapi import Depends
from jose import jwt, JWTError
from passlib.context import CryptContext

from models.domain.UserModel import UserModel
from repositories.UserRepository import UserRepository
from configs import security as security_config


class UserSecurityService:
    user_repository: UserRepository

    def __init__(self, user_repository: UserRepository = Depends()) -> None:
        self.__user_repository = user_repository
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.__pwd_context.hash(password)

    def register_user(self, username, password):
        if self.__user_repository.is_username_exists(username):
            return False
        try:
            hashed_password = self.__pwd_context.hash(password)
            user = UserModel(username=username, hashed_password=hashed_password)
            self.__user_repository.create(user)
        except Exception as e:
            return False
        return True

    def authorizate_user(self, username: str, password: str):
        user = self.__user_repository.get_user_by_username(username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def authenticate_user(self, access_token: str):
        try:
            payload = jwt.decode(access_token, security_config.SECRET_KEY, algorithms=[security_config.ALGORITHM])
            username: str = payload.get("sub")
        except JWTError:
            return None

        user = self.__user_repository.get_user_by_username(username)
        return user

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        to_encode.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(
            minutes=security_config.ACCESS_TOKEN_EXPIRE_MINUTES)})
        return jwt.encode(to_encode, security_config.SECRET_KEY, algorithm=security_config.ALGORITHM)

    @staticmethod
    def decode_access_token(token: str):
        try:
            encoded_jwt = jwt.decode(token, security_config.SECRET_KEY, algorithms=[security_config.ALGORITHM])
        except jwt.JWSError:
            return None
        return encoded_jwt
