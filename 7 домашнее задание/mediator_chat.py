from abc import ABC, abstractmethod
from typing import List

class IMediator(ABC):
    @abstractmethod
    def send(self, message: str, user: 'User'):
        pass

class ChatRoom(IMediator):
    def __init__(self):
        self.users: List['User'] = []

    def add_user(self, user: 'User'):
        self.users.append(user)
        self.broadcast(f"{user.name} присоединился к чату")

    def remove_user(self, user: 'User'):
        if user in self.users:
            self.users.remove(user)
            self.broadcast(f"{user.name} покинул чат")

    def send(self, message: str, sender: 'User'):
        for user in self.users:
            if user != sender:
                user.receive(message)

    def broadcast(self, message: str):
        for user in self.users:
            user.receive(f"[Система] {message}")

class User:
    def __init__(self, name: str, mediator: IMediator):
        self.name = name
        self.mediator = mediator

    def send(self, message: str):
        print(f"{self.name} → {message}")
        self.mediator.send(message, self)

    def receive(self, message: str):
        print(f"    {self.name} получил: {message}")

if __name__ == "__main__":
    chat = ChatRoom()

    alice = User("Алиса", chat)
    bob = User("Боб", chat)
    carl = User("Карл", chat)

    chat.add_user(alice)
    chat.add_user(bob)
    chat.add_user(carl)

    alice.send("Всем привет!")
    bob.send("Как дела?")
    carl.send("Отлично, а у вас?")

    chat.remove_user(bob)