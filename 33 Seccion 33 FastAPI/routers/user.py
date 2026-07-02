from typing import List

from fastapi import APIRouter, Depends
from starlette import status

from dependencies.security import get_current_user
from dependencies.user_dependencies import get_user_service
from models.user import User
from services.user_service import ServiceUser

router_user = APIRouter()

@router_user.get('/data', tags=['User'], response_model=List[User] | None)
def get_user(service : ServiceUser = Depends(get_user_service),
             current_user = Depends(get_current_user)) -> List[User] | None: # Con que este ya sirve para proteger la ruta
    return service.get_all()

@router_user.get('/user/id/{id_user}', tags=['User'], response_model=User | None)
def get_user_by_id(id_user: int,
                   service : ServiceUser = Depends(get_user_service)) -> User | None:
    return service.get_by_id(id_user)

@router_user.get('/user/gmail/{gmail_user}', tags=['User'], response_model=User | None)
def get_user_by_gmail(gmail_user: str,
                   service : ServiceUser = Depends(get_user_service),
                   current_user = Depends(get_current_user)) -> User | None:
    return service.get_by_gmail(gmail_user)

@router_user.post('/user/create', tags=['User'], response_model=User | None)
def create_user(email : str,
                password : str,
                active: bool,
                service : ServiceUser = Depends(get_user_service)) -> User | None:
    return service.create_user(email, password, active)