from abc import ABC, abstractmethod
from typing import List, Optional

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def on(self): print("Свет включён")
    def off(self): print("Свет выключен")

class TV:
    def on(self): print("Телевизор включён")
    def off(self): print("Телевизор выключен")

class AirConditioner:
    def on(self): print("Кондиционер включён")
    def off(self): print("Кондиционер выключен")

class MacroCommand(ICommand):
    def __init__(self, commands: List[ICommand]):
        self.commands = commands

    def execute(self):
        for cmd in self.commands:
            cmd.execute()

    def undo(self):
        for cmd in reversed(self.commands):
            cmd.undo()

class NoCommand(ICommand):
    def execute(self): pass
    def undo(self): pass

class RemoteControl:
    def __init__(self, slots: int = 5):
        self.on_commands: List[ICommand] = [NoCommand()] * slots
        self.off_commands: List[ICommand] = [NoCommand()] * slots
        self.undo_stack: List[ICommand] = []

    def set_command(self, slot: int, on: ICommand, off: ICommand):
        self.on_commands[slot] = on
        self.off_commands[slot] = off

    def on_button_pressed(self, slot: int):
        if slot < len(self.on_commands):
            self.on_commands[slot].execute()
            self.undo_stack.append(self.on_commands[slot])

    def off_button_pressed(self, slot: int):
        if slot < len(self.off_commands):
            self.off_commands[slot].execute()
            self.undo_stack.append(self.off_commands[slot])

    def undo_button_pressed(self):
        if self.undo_stack:
            cmd = self.undo_stack.pop()
            cmd.undo()

if __name__ == "__main__":
    remote = RemoteControl(4)

    light = Light()
    tv = TV()
    ac = AirConditioner()

    remote.set_command(0, LightOn := type('LightOn', (ICommand,), {'execute': light.on, 'undo': light.off})(),
                          LightOff := type('LightOff', (ICommand,), {'execute': light.off, 'undo': light.on})())

    remote.set_command(1, TVOn := type('TVOn', (ICommand,), {'execute': tv.on, 'undo': tv.off})(),
                          TVOff := type('TVOff', (ICommand,), {'execute': tv.off, 'undo': tv.on})())

    movie_macro = MacroCommand([TVOn, LightOff])

    remote.set_command(2, movie_macro, MacroCommand([TVOff, LightOn]))

    print("Тест пульта:")
    remote.on_button_pressed(0)
    remote.on_button_pressed(1)
    remote.on_button_pressed(2)
    print("\nОтмена:")
    remote.undo_button_pressed()
    remote.undo_button_pressed()
    remote.undo_button_pressed()