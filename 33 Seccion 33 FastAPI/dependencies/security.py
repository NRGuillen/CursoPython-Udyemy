from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from config.settings import Settings, settings
from dependencies.user_dependencies import get_user_service
from services.user_service import ServiceUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token") # Este token tiene que coincidir con el que retorna la ruta /token

def get_current_user(
                    token : str = Depends(oauth2_scheme),
                    user: ServiceUser = Depends(get_user_service)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        user_gmail : str | None = payload.get('sub')
    except (JWTError, TypeError, ValueError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

    user_auth = user.get_by_gmail(user_gmail)
    if not user_auth:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find user")
    return user_auth