from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from dependencies.user_dependencies import get_user_service
from models.auth import Token, LoginRequest
from security.jwt import create_access_token_jwt
from services.user_service import ServiceUser

router_auth = APIRouter()
@router_auth.post('/token', response_model=Token)
def login(data : LoginRequest,
          service : ServiceUser= Depends(get_user_service))-> Token | HTTPException:
    user = service.get_by_gmail(data.email)
    if not user or not data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    token = create_access_token_jwt(subjet=data.email)
    return Token(access_token=token)