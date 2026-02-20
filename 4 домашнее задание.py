from abc import ABC, abstractmethod
from typing import Optional


class IVehicle(ABC):
    @abstractmethod
    def drive(self) -> None:
        pass

    @abstractmethod
    def refuel(self) -> None:
        pass


class Car(IVehicle):
    def __init__(self, brand: str, model: str, fuel_type: str):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def drive(self) -> None:
        print(f"Car {self.brand} {self.model} is driving on {self.fuel_type}")

    def refuel(self) -> None:
        print(f"Refueling {self.brand} {self.model} → {self.fuel_type}")


class Motorcycle(IVehicle):
    def __init__(self, moto_type: str, engine_cc: int):
        self.moto_type = moto_type
        self.engine_cc = engine_cc

    def drive(self) -> None:
        print(f"Motorcycle {self.moto_type} ({self.engine_cc} cc) is riding")

    def refuel(self) -> None:
        print(f"Refueling motorcycle {self.moto_type}")


class Truck(IVehicle):
    def __init__(self, capacity_tons: float, axles: int):
        self.capacity_tons = capacity_tons
        self.axles = axles

    def drive(self) -> None:
        print(f"Truck ({self.axles} axles, {self.capacity_tons} t) is transporting cargo")

    def refuel(self) -> None:
        print("Refueling truck → diesel")


class Bus(IVehicle):
    def __init__(self, seats: int, route: str):
        self.seats = seats
        self.route = route

    def drive(self) -> None:
        print(f"Bus on route {self.route} (seats: {self.seats}) is moving")

    def refuel(self) -> None:
        print("Refueling bus")


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> IVehicle:
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> IVehicle:
        brand = input("Car brand: ").strip() or "Toyota"
        model = input("Model: ").strip() or "Camry"
        fuel = input("Fuel type (gas/diesel/electric): ").strip() or "gas"
        return Car(brand, model, fuel)


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self) -> IVehicle:
        moto_type = input("Motorcycle type (sport/touring): ").strip() or "sport"
        try:
            cc = int(input("Engine capacity (cc): ") or 600)
        except ValueError:
            cc = 600
        return Motorcycle(moto_type, cc)


class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> IVehicle:
        try:
            tons = float(input("Load capacity (tons): ") or 20)
            axles = int(input("Number of axles: ") or 3)
        except ValueError:
            tons, axles = 20, 3
        return Truck(tons, axles)


class BusFactory(VehicleFactory):
    def create_vehicle(self) -> IVehicle:
        try:
            seats = int(input("Number of seats: ") or 45)
        except ValueError:
            seats = 45
        route = input("Route: ").strip() or "Almaty–Astana"
        return Bus(seats, route)


def main():
    factories = {
        "1": ("Car", CarFactory()),
        "2": ("Motorcycle", MotorcycleFactory()),
        "3": ("Truck", TruckFactory()),
        "4": ("Bus", BusFactory()),
    }

    print("Select vehicle type:")
    for key, (name, _) in factories.items():
        print(f"  {key}) {name}")

    choice = input("\n→ ").strip()

    if choice not in factories:
        print("Invalid choice")
        return

    name, factory = factories[choice]
    print(f"\nCreating: {name}")
    vehicle = factory.create_vehicle()
    vehicle.drive()
    vehicle.refuel()


if __name__ == "__main__":
    main()