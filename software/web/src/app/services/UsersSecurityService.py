import datetime

from fastapi import Depends
from jose import jwt

from repositories.UserRepository import UserRepository

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from configs import security as security_config


class UsersSecurityService:
    user_repository: UserRepository

    def __init__(self, user_repository: UserRepository = Depends()) -> None:
        self.__user_repository = user_repository
        self.__pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.__oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def verify_password(self, plain_password, hashed_password):
        return self.__pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.__pwd_context.hash(password)

    def authenticate_user(self, username: str, password: str):
        user = self.__user_repository.get_user_by_username(username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
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
