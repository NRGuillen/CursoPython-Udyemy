from typing import List

from fastapi import APIRouter
from fastapi.params import Depends

from dependencies.message_dependencies import get_message_service
from models.message import Messages
from models.message_entity import MessagesEntity
from services.message_service import MessageService

# Lo reemplazamos por message_service
#example_messages : List[Messages] = [
#    Messages(id = 1, name = 'Ruben'),
#    Messages(id = 1, name = 'Javier'),
#    Messages(id = 1, name = 'Daniel')
#]

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
def read_mesages(service: MessageService = Depends(get_message_service)):
    """Depends(get_message_service) return MessageService() -|> service = MessageService() -|> service.get_all()
    El depends sirve para indicar a la ruta donde se encuentran los datos,

    DEPENDENCIES
    def get_message_service() -> MessageService:
        return MessageService()

    Como get_message_service retorna un objeto de MessageService, service pasa a ser un objeto de MessageService y
    nos permite utilizar la logica de sus metodos sin mezclarl la logica dentro de esta ruta

    service: MessageService = Depends(get_message_service) ==  service = MessageService
    """
    return service.get_all()  # 'hola' -> Expected type 'list[Messages]', got 'str' instead

@router.get('/entity', response_model=List[MessagesEntity])
def full_user() -> list[MessagesEntity] :
    return data

@router.get('/ejemplo', response_model=dict)
def ejemplo() -> dict:
    return {
     'message' :  'esto es un ejemplo de router en FastAPI'
    }