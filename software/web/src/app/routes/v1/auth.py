from fastapi import APIRouter, HTTPException, status, Depends
from models.viewout.token import Token, Login
from services import UserSecurityService


AuthRouter = APIRouter(prefix='/auth')


@AuthRouter.post("/", response_model=Token)
async def login(login: Login, users_security_service: UserSecurityService = Depends()):
    if not users_security_service.authorizate_user(login.username, login.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    return Token(
        access_token=users_security_service.create_access_token({"sub": login.username}),
        token_type="Bearer"
    )


async def get_current_user(token: Token, users_security_service: UserSecurityService = Depends()):
    user = users_security_service.authenticate_user(token.access_token, token.token_type)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user.name
