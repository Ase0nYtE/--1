from abc import ABC, abstractmethod

class Beverage(ABC):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def boil_water(self):
        print("Кипятим воду")

    def pour_in_cup(self):
        print("Наливаем в чашку")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def customer_wants_condiments(self) -> bool:
        return True

class Tea(Beverage):
    def brew(self):
        print("Завариваем чай")

    def add_condiments(self):
        print("Добавляем лимон")

class Coffee(Beverage):
    def brew(self):
        print("Варим кофе")

    def add_condiments(self):
        print("Добавляем сахар и молоко")

    def customer_wants_condiments(self) -> bool:
        return input("Добавить сахар и молоко? (y/n): ").lower() == 'y'

if __name__ == "__main__":
    print("Приготовление чая:")
    tea = Tea()
    tea.prepare_recipe()

    print("\nПриготовление кофе:")
    coffee = Coffee()
    coffee.prepare_recipe()