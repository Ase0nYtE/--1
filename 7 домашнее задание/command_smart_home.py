from abc import ABC, abstractmethod
from typing import List

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def turn_on(self):
        print("Свет включён")

    def turn_off(self):
        print("Свет выключен")

class Door:
    def open(self):
        print("Дверь открыта")

    def close(self):
        print("Дверь закрыта")

class Thermostat:
    def __init__(self):
        self.temperature = 22

    def increase(self):
        self.temperature += 1
        print(f"Температура увеличена → {self.temperature}°C")

    def decrease(self):
        self.temperature -= 1
        print(f"Температура уменьшена → {self.temperature}°C")

class LightOnCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

class DoorOpenCommand(ICommand):
    def __init__(self, door: Door):
        self.door = door

    def execute(self):
        self.door.open()

    def undo(self):
        self.door.close()

class ThermostatUpCommand(ICommand):
    def __init__(self, thermostat: Thermostat):
        self.thermostat = thermostat

    def execute(self):
        self.thermostat.increase()

    def undo(self):
        self.thermostat.decrease()

class RemoteControl:
    def __init__(self):
        self.command: ICommand | None = None
        self.history: List[ICommand] = []

    def set_command(self, command: ICommand):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
            self.history.append(self.command)

    def undo_last(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()
            print("Отменена последняя команда")

if __name__ == "__main__":
    light = Light()
    door = Door()
    thermo = Thermostat()

    remote = RemoteControl()

    remote.set_command(LightOnCommand(light))
    remote.press_button()

    remote.set_command(DoorOpenCommand(door))
    remote.press_button()

    remote.set_command(ThermostatUpCommand(thermo))
    remote.press_button()
    remote.press_button()

    print("\nОтмена:")
    remote.undo_last()
    remote.undo_last()
    remote.undo_last()