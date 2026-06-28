from pydantic import BaseModel

class MessagesEntity(BaseModel):
    id: int
    name: str
    password: str