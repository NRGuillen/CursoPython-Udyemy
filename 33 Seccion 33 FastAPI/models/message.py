from pydantic import BaseModel, Field


# BaseModel nos permite definir el modelo de datos que vamos a usar con validacion automatica, es decir que si
# el id es un int y le pasamos un nombre, daria error
class Messages(BaseModel):
    id: int | None = None # None = opcional
    name: str = Field(...,
                      min_length=1 ,
                      max_length=100,
                      description='Contenido del mensaje entre 1 y 100 chars') # ... -> requerido

