from typing import List

from models.message import Messages

class MessageService:
    def __init__(self):
        self.messages : List[Messages] = [
            Messages(id=1, name='Ruben'),
            Messages(id=2, name='Javier'),
            Messages(id=3, name='Daniel')
        ]
        self.next_id = len(self.messages)+1

    def get_all(self) -> List[Messages]:
        return self.messages

    def get_by_id(self, id_find: int) -> Messages | None:
        for ids in self.messages:
            if ids.id == id_find:
                return ids
        return None

    def create( self, new_message: Messages ) -> Messages:
        new_message.id = self.next_id
        self.messages.append(new_message)
        return new_message

    def update(self, message_id : int, name : Messages) -> Messages | None:
        posicion = 0
        for message in self.messages:
            if message.id == message_id:
                update = Messages(id=message.id, name=name.name)
                self.messages[posicion] = update
                return update
            posicion += 1
        return None

    def delete(self, message_id : int) -> bool:
        posicion = 0
        for message in self.messages:
            if message.id == message_id:
                del self.messages[posicion]
                return True
            posicion += 1
        return False