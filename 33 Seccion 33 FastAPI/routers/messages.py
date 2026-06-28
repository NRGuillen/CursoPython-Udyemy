from typing import List

from fastapi import APIRouter

from models.message import Messages
from models.message_entity import MessagesEntity

example_messages : List[Messages] = [
    Messages(id = 1, name = 'Ruben'),
    Messages(id = 1, name = 'Javier'),
    Messages(id = 1, name = 'Daniel')
]

data : List[MessagesEntity] = [
    MessagesEntity(id= 1, name='Ruben', password = 'fhjksaf'),
    MessagesEntity(id=2, name='Javier', password='gfdgdsda'),
    #{
    #    'id' : 1,
    #    'name' : 'Ruben',
    #    'password' : 'jahfhjsa' # Como la ruta va a responder con datos list[Messages] Messages no tiene el parametro
    #                            # password, por lo tanto solo mostrara el id y el name, eso es lo bueno de usar el
    #                            # response_model que tiene fuerte tipado, en cambio con list[MessagesEntity] no pasaria
    #},
    ]

router = APIRouter()
@router.get('/', response_model=List[Messages]) # response_model nos indica que va a retornar, fuertemente tipado
def read_mesages() -> List[Messages] :
    return example_messages # 'hola' -> Expected type 'list[Messages]', got 'str' instead

@router.get('/entity', response_model=List[MessagesEntity])
def full_user() -> list[MessagesEntity] :
    return data

@router.get('/ejemplo', response_model=dict)
def ejemplo() -> dict:
    return {
     'message' :  'esto es un ejemplo de router en FastAPI'
    }