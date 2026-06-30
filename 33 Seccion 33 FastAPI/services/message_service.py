from typing import List

from models.message import Messages

class MessageService:
    def __init__(self):
        self.messages : List[Messages] = [
            Messages(id=1, name='Ruben'),
            Messages(id=2, name='Javier'),
            Messages(id=3, name='Daniel')
        ]

    def get_all(self) -> List[Messages]:
        return self.messages

    def get_by_id(self, id_find: int) -> Messages | None:
        for ids in self.messages:
            if ids.id == id_find:
                return ids
        return None