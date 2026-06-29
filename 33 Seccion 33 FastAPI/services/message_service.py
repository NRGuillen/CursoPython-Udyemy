from typing import List

from models.message import Messages

class MessageService:
    def __init__(self):
        self.messages : List[Messages] = [
            Messages(id=1, name='Ruben'),
            Messages(id=1, name='Javier'),
            Messages(id=1, name='Daniel')
        ]

    def get_all(self) -> List[Messages]:
        return self.messages
