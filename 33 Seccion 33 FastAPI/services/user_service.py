from typing import List

from models.user import User


class ServiceUser:
    def __init__(self):
        self.users : List[User] = [
            User(id=1, email='ruben@gmail.com', password='prueba123', active=True),
            User(id=2, email='Javier@gmail.com', password='prueba123', active=True),
            User(id=3, email='Daniel@gmail.com', password='prueba123', active=True),
        ]
        self.next_id = len(self.users)+1

    def get_all(self) -> List[User]:
        return self.users

    def get_by_id(self, id_user: int) -> User | None:
        for user in self.users:
            if user.id == id_user:
                return user
        return None

    def get_by_gmail(self, email: str | None) -> User | None:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def create_user(self, email: str, password: str, active : bool) -> User:
        user = User(id = self.next_id, email=email, password=password, active=active)
        self.users.append(user)
        return user


