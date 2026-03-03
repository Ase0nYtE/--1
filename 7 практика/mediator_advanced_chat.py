from abc import ABC, abstractmethod
from typing import Dict, List

class IMediator(ABC):
    @abstractmethod
    def send(self, message: str, user: 'User', channel: str):
        pass

    @abstractmethod
    def add_user(self, user: 'User', channel: str):
        pass

    @abstractmethod
    def remove_user(self, user: 'User', channel: str):
        pass

class ChatMediator(IMediator):
    def __init__(self):
        self.channels: Dict[str, List['User']] = {}

    def add_user(self, user: 'User', channel: str):
        if channel not in self.channels:
            self.channels[channel] = []
        if user not in self.channels[channel]:
            self.channels[channel].append(user)
            self.broadcast(channel, f"[Система] {user.name} присоединился к каналу {channel}")

    def remove_user(self, user: 'User', channel: str):
        if channel in self.channels and user in self.channels[channel]:
            self.channels[channel].remove(user)
            self.broadcast(channel, f"[Система] {user.name} покинул канал {channel}")

    def send(self, message: str, sender: 'User', channel: str):
        if channel not in self.channels:
            print(f"Канал {channel} не существует")
            return
        for user in self.channels[channel]:
            if user != sender:
                user.receive(message, channel)

    def broadcast(self, channel: str, message: str):
        if channel in self.channels:
            for user in self.channels[channel]:
                user.receive(message, channel)

class User:
    def __init__(self, name: str, mediator: IMediator):
        self.name = name
        self.mediator = mediator

    def send(self, message: str, channel: str):
        print(f"[{channel}] {self.name} → {message}")
        self.mediator.send(message, self, channel)

    def receive(self, message: str, channel: str):
        print(f"    [{channel}] {self.name} получил: {message}")

if __name__ == "__main__":
    mediator = ChatMediator()

    alice = User("Алиса", mediator)
    bob = User("Боб", mediator)
    carl = User("Карл", mediator)

    alice_channel = "general"
    bob_channel = "work"

    mediator.add_user(alice, alice_channel)
    mediator.add_user(bob, bob_channel)
    mediator.add_user(carl, alice_channel)

    alice.send("Всем привет в общем чате!", alice_channel)
    carl.send("Привет, Алиса!", alice_channel)

    bob.send("Коллеги, дедлайн завтра", bob_channel)

    mediator.remove_user(carl, alice_channel)