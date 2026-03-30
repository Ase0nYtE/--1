from abc import ABC, abstractmethod
from typing import List

class OrganizationComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_budget(self) -> float:
        pass

    @abstractmethod
    def get_employee_count(self) -> int:
        pass

    @abstractmethod
    def display(self, level: int = 0):
        pass

class Employee(OrganizationComponent):
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_name(self) -> str:
        return self.name

    def get_budget(self) -> float:
        return self.salary

    def get_employee_count(self) -> int:
        return 1

    def display(self, level: int = 0):
        indent = "  " * level
        print(f"{indent}├─ {self.name} ({self.position}) — {self.salary:,.0f} ₸")

class Contractor(Employee):
    def get_budget(self) -> float:
        return 0.0  # Контракторы не входят в бюджет отдела

    def display(self, level: int = 0):
        indent = "  " * level
        print(f"{indent}├─ {self.name} (Контрактор, {self.position}) — {self.salary:,.0f} ₸ (не в бюджете)")

class Department(OrganizationComponent):
    def __init__(self, name: str):
        self.name = name
        self.components: List[OrganizationComponent] = []

    def add(self, component: OrganizationComponent):
        self.components.append(component)

    def remove(self, component: OrganizationComponent):
        if component in self.components:
            self.components.remove(component)

    def get_name(self) -> str:
        return self.name

    def get_budget(self) -> float:
        return sum(comp.get_budget() for comp in self.components)

    def get_employee_count(self) -> int:
        return sum(comp.get_employee_count() for comp in self.components)

    def display(self, level: int = 0):
        indent = "  " * level
        print(f"{indent}└─ Отдел: {self.name} (сотрудников: {self.get_employee_count()}, бюджет: {self.get_budget():,.0f} ₸)")
        for comp in self.components:
            comp.display(level + 1)

    def find_employee(self, name: str) -> OrganizationComponent | None:
        for comp in self.components:
            if isinstance(comp, Employee) and comp.get_name().lower() == name.lower():
                return comp
            if isinstance(comp, Department):
                found = comp.find_employee(name)
                if found:
                    return found
        return None

if __name__ == "__main__":
    # Создаём структуру компании
    company = Department("xAI Компания")

    it_dept = Department("IT-отдел")
    marketing_dept = Department("Маркетинг")
    finance_dept = Department("Финансы")

    company.add(it_dept)
    company.add(marketing_dept)
    company.add(finance_dept)

    # IT отдел
    it_dept.add(Employee("Асет", "Senior Developer", 850000))
    it_dept.add(Employee("Айдар", "DevOps Engineer", 720000))
    it_dept.add(Contractor("Иван", "Внешний разработчик", 450000))

    # Маркетинг
    marketing_dept.add(Employee("Дина", "Marketing Manager", 650000))
    marketing_dept.add(Employee("Ерлан", "SMM Specialist", 480000))

    # Финансы
    finance_dept.add(Employee("Мария", "Chief Accountant", 780000))

    # Подотдел в IT
    backend_team = Department("Backend Team")
    backend_team.add(Employee("Боб", "Backend Developer", 650000))
    it_dept.add(backend_team)

    print("=== Структура организации ===\n")
    company.display()

    print("\n=== Общая информация ===")
    print(f"Общий бюджет компании: {company.get_budget():,.0f} ₸")
    print(f"Общее количество сотрудников: {company.get_employee_count()}")

    # Поиск сотрудника
    found = company.find_employee("Асет")
    if found:
        print(f"\nНайден сотрудник: {found.get_name()} — {found.get_budget():,.0f} ₸")