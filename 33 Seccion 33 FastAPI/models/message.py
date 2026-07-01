from pydantic import BaseModel

# BaseModel nos permite definir el modelo de datos que vamos a usar con validacion automatica, es decir que si
# el id es un int y le pasamos un nombre, daria error
class Messages(BaseModel):
    id: int | None = None
    name: str