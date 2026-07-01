from typing import List

from fastapi import APIRouter, HTTPException, Depends
from fastapi.params import Query
from starlette import status

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

# Ruta variable http://127.0.0.1:8000/messages/find/1
@router.get('/find/{id_find}', response_model= Messages | None)
def find_messages(id_find : int, service: MessageService = Depends(get_message_service)):
    message = service.get_by_id(id_find)
    if message is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Mensaje con id {id_find} no existe')
    return message

# Ruta con querrys http://127.0.0.1:8000/messages/details?message_id=1
@router.get('/details', response_model= Messages | None)
def get_message_url_params(name : str,
                           #message_id : int = 2, # Este campo pasa a ser opciona, ya que insertamos un valor por defecto
                           message_id : int = Query(..., ge=1) , # Valor obligatorio y mayor o igual a 1
                           # Query(3, ge=1), # El query quiere decir que el valor por defecto
                           # si no mete nada el usuario es 3, y si mete uno tiene que ser mayor o igual a 1 ge = greater or equal, hay mas funciones que ge
                           service: MessageService = Depends(get_message_service)):
    print(name)
    return service.get_by_id(message_id)

@router.post('/create', response_model=Messages, status_code=status.HTTP_201_CREATED)
def create_messages(message : Messages,
                    service: MessageService = Depends(get_message_service)) -> Messages:
    return service.create(message)

@router.put('/update/{id_update}', response_model=Messages, status_code=status.HTTP_200_OK)
def update_messages(id_update : int,
                    message : Messages,
                    service: MessageService = Depends(get_message_service)):
    message_update =  service.update(id_update, message)
    if message_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Mensaje con id {id_update} no existe'
                            )
    return message_update

@router.delete('/delete/{id_delete}', status_code=status.HTTP_204_NO_CONTENT)
def delete_messages(id_delete : int, service: MessageService = Depends(get_message_service)):
    deleted =  service.delete(id_delete)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Mensaje con id {id_delete} no existe')
