from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


class ServiceClass(Enum):
    ECONOMY = 1.0
    BUSINESS = 1.6


@dataclass
class Trip:
    distance_km: float
    passengers: int = 1
    service_class: ServiceClass = ServiceClass.ECONOMY
    child_discount: bool = False
    pensioner_discount: bool = False
    extra_luggage: bool = False


class ICostCalculationStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, trip: Trip) -> float:
        pass


class AirplaneStrategy(ICostCalculationStrategy):
    def calculate_cost(self, trip: Trip) -> float:
        base = trip.distance_km * 12
        base *= trip.service_class.value
        base *= trip.passengers

        if trip.child_discount:
            base *= 0.75
        if trip.pensioner_discount:
            base *= 0.85

        if trip.extra_luggage:
            base += 3500

        return round(base, 2)


class TrainStrategy(ICostCalculationStrategy):
    def calculate_cost(self, trip: Trip) -> float:
        base = trip.distance_km * 5.5
        base *= trip.service_class.value
        base *= trip.passengers

        if trip.child_discount:
            base *= 0.6
        if trip.pensioner_discount:
            base *= 0.8

        return round(base, 2)


class BusStrategy(ICostCalculationStrategy):
    def calculate_cost(self, trip: Trip) -> float:
        base = trip.distance_km * 3.2
        base *= trip.passengers

        if trip.child_discount:
            base *= 0.5
        if trip.pensioner_discount:
            base *= 0.7

        if trip.extra_luggage:
            base += 800

        return round(base, 2)


class TravelBookingContext:
    def __init__(self, strategy: ICostCalculationStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: ICostCalculationStrategy):
        self.strategy = strategy

    def calculate_trip_cost(self, trip: Trip) -> float:
        if self.strategy is None:
            raise ValueError("Стратегия не выбрана")
        return self.strategy.calculate_cost(trip)


if __name__ == "__main__":
    trip = Trip(distance_km=1200, passengers=2, service_class=ServiceClass.BUSINESS,
                child_discount=True, extra_luggage=True)

    ctx = TravelBookingContext()

    ctx.set_strategy(AirplaneStrategy())
    print(f"Самолёт: {ctx.calculate_trip_cost(trip)} ₸")

    ctx.set_strategy(TrainStrategy())
    print(f"Поезд:   {ctx.calculate_trip_cost(trip)} ₸")

    ctx.set_strategy(BusStrategy())
    print(f"Автобус: {ctx.calculate_trip_cost(trip)} ₸")