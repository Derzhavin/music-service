from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.models.view.user import UserIn
from app.services import UserSecurityService


SecurityRouter = APIRouter(prefix='/v1/users')


@SecurityRouter.post("/login", tags=['users'])
async def login(form_data: OAuth2PasswordRequestForm = Depends(), users_security_service: UserSecurityService = Depends()):
    user = users_security_service.authorizate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {
        'access_token' :users_security_service.create_access_token({"sub": user.username}),
        'token_type' : "bearer"
    }


async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl='/v1/users/login')), users_security_service: UserSecurityService = Depends()):
    user = users_security_service.authenticate_user(token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user.username


@SecurityRouter.post("/register", tags=['users'])
async def register_user(user_in: UserIn, user_security_service: UserSecurityService = Depends()):
    res = user_security_service.register_user(user_in.username, user_in.password)

    if res:
        return status.HTTP_201_CREATED
    return status.HTTP_409_CONFLICT
