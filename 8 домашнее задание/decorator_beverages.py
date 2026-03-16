from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass

class Espresso(Beverage):
    def get_description(self) -> str:
        return "Эспрессо"

    def cost(self) -> float:
        return 800.0

class Tea(Beverage):
    def get_description(self) -> str:
        return "Чай"

    def cost(self) -> float:
        return 500.0

class Latte(Beverage):
    def get_description(self) -> str:
        return "Латте"

    def cost(self) -> float:
        return 1200.0

class Mocha(Beverage):
    def get_description(self) -> str:
        return "Мокко"

    def cost(self) -> float:
        return 1400.0

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_description(self) -> str:
        return self._beverage.get_description()

    def cost(self) -> float:
        return self._beverage.cost()

class Milk(BeverageDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + " + молоко"

    def cost(self) -> float:
        return self._beverage.cost() + 300.0

class Sugar(BeverageDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + " + сахар"

    def cost(self) -> float:
        return self._beverage.cost() + 100.0

class WhippedCream(BeverageDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + " + взбитые сливки"

    def cost(self) -> float:
        return self._beverage.cost() + 400.0

class Chocolate(BeverageDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + " + шоколад"

    def cost(self) -> float:
        return self._beverage.cost() + 350.0

class Cinnamon(BeverageDecorator):
    def get_description(self) -> str:
        return self._beverage.get_description() + " + корица"

    def cost(self) -> float:
        return self._beverage.cost() + 150.0

if __name__ == "__main__":
    print("Заказ 1:")
    drink = Espresso()
    drink = Milk(drink)
    drink = Sugar(drink)
    print(f"{drink.get_description()} → {drink.cost()} ₸")

    print("\nЗаказ 2:")
    drink = Latte()
    drink = WhippedCream(drink)
    drink = Chocolate(drink)
    drink = Cinnamon(drink)
    print(f"{drink.get_description()} → {drink.cost()} ₸")

    print("\nЗаказ 3:")
    drink = Mocha()
    drink = Milk(drink)
    drink = Milk(drink)
    drink = Sugar(drink)
    print(f"{drink.get_description()} → {drink.cost()} ₸")

    print("\nЗаказ 4:")
    drink = Tea()
    drink = Chocolate(drink)
    print(f"{drink.get_description()} → {drink.cost()} ₸")