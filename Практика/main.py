# main.py
# Бұл файл екі практикалық жұмысты қамтиды:
# 1. Модуль 01: Көлік құралдарын басқару жүйесі
# 2. Модуль 02: Пайдаланушыларды басқару жүйесі

# ==============================
# МОДУЛЬ 01: КӨЛІК ҚҰРАЛДАРЫН БАСҚАРУ ЖҮЙЕСІ
# ==============================

class Vehicle:
    """Негізгі көлік құралы класы"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_running = False

    def start_engine(self):
        """Қозғалтқышты іске қосу"""
        if not self.engine_running:
            self.engine_running = True
            return f"{self.brand} {self.model} қозғалтқышы іске қосылды"
        return f"{self.brand} {self.model} қозғалтқышы қазірдің өзінде жұмыс істеп тұр"

    def stop_engine(self):
        """Қозғалтқышты өшіру"""
        if self.engine_running:
            self.engine_running = False
            return f"{self.brand} {self.model} қозғалтқышы өшірілді"
        return f"{self.brand} {self.model} қозғалтқышы қазірдің өзінде өшірілген"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Car(Vehicle):
    """Автомобиль класы - Vehicle класынан мұраланады"""

    def __init__(self, brand, model, year, doors, transmission):
        super().__init__(brand, model, year)
        self.doors = doors
        self.transmission = transmission  # transmission типі: автоматты немесе механикалық

    def __str__(self):
        return f"{super().__str__()} - {self.doors} есік, {self.transmission} трансмиссия"


class Motorcycle(Vehicle):
    """Мотоцикл класы - Vehicle класынан мұраланады"""

    def __init__(self, brand, model, year, body_type, has_storage):
        super().__init__(brand, model, year)
        self.body_type = body_type  # body_type: спорттық, классикалық, т.б.
        self.has_storage = has_storage  # has_storage: багажтық қорап бар ма?

    def __str__(self):
        storage_info = "багажтық қорап бар" if self.has_storage else "багажтық қорап жоқ"
        return f"{super().__str__()} - {self.body_type} тип, {storage_info}"


class Garage:
    """Гараж класы - көлік құралдарының тізімін басқарады (композиция)"""

    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Гаражға көлік құралын қосу"""
        self.vehicles.append(vehicle)
        return f"'{vehicle.brand} {vehicle.model}' гараж '{self.name}' қосылды"

    def remove_vehicle(self, brand, model):
        """Гараждан көлік құралын жою"""
        for vehicle in self.vehicles:
            if vehicle.brand == brand and vehicle.model == model:
                self.vehicles.remove(vehicle)
                return f"'{brand} {model}' гараж '{self.name}' жойылды"
        return f"'{brand} {model}' гараж '{self.name}' табылмады"

    def show_vehicles(self):
        """Гараждағы барлық көлік құралдарын көрсету"""
        if not self.vehicles:
            return f"Гараж '{self.name}' бос"

        result = f"\n=== ГАРАЖ '{self.name}' ===\n"
        for i, vehicle in enumerate(self.vehicles, 1):
            result += f"{i}. {vehicle}\n"
        return result

    def __str__(self):
        return f"Гараж '{self.name}' ({len(self.vehicles)} көлік)"


class Fleet:
    """Автопарк класы - гараждардың тізімін басқарады (композиция)"""

    def __init__(self, name):
        self.name = name
        self.garages = []

    def add_garage(self, garage):
        """Автопаркқа гараж қосу"""
        self.garages.append(garage)
        return f"Гараж '{garage.name}' автопарк '{self.name}' қосылды"

    def remove_garage(self, garage_name):
        """Автопарктан гараж жою"""
        for garage in self.garages:
            if garage.name == garage_name:
                self.garages.remove(garage)
                return f"Гараж '{garage_name}' автопарк '{self.name}' жойылды"
        return f"Гараж '{garage_name}' автопарк '{self.name}' табылмады"

    def find_vehicle(self, brand, model):
        """Автопарктан көлік құралын іздеу"""
        found_vehicles = []

        for garage in self.garages:
            for vehicle in garage.vehicles:
                if vehicle.brand == brand and vehicle.model == model:
                    found_vehicles.append((vehicle, garage))

        return found_vehicles

    def show_all_vehicles(self):
        """Автопарктағы барлық көлік құралдарын көрсету"""
        if not self.garages:
            return f"Автопарк '{self.name}' бос"

        result = f"\n=== АВТОПАРК '{self.name}' ===\n"
        total_vehicles = 0

        for garage in self.garages:
            result += f"\n{garage}:\n"
            for i, vehicle in enumerate(garage.vehicles, 1):
                result += f"  {i}. {vehicle}\n"
            total_vehicles += len(garage.vehicles)

        result += f"\nБарлығы: {total_vehicles} көлік"
        return result

    def __str__(self):
        total_vehicles = sum(len(garage.vehicles) for garage in self.garages)
        return f"Автопарк '{self.name}' ({len(self.garages)} гараж, {total_vehicles} көлік)"


# ==============================
# МОДУЛЬ 02: ПАЙДАЛАНУШЫЛАРДЫ БАСҚАРУ ЖҮЙЕСІ
# (YAGNI, KISS, DRY ПРИНЦИПТЕРІН ҚОЛДАНА ОТЫРЫП)
# ==============================

class User:
    """Пайдаланушы класы - тек қажетті қасиеттермен (KISS принципі)"""

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.role}"


class UserManager:
    """Пайдаланушыларды басқару класы (YAGNI принципі - тек қажетті функционалдық)"""

    def __init__(self):
        self.users = []

    def add_user(self, name, email, role="User"):
        """Жаңа пайдаланушыны қосу (KISS - қарапайым әдіс)"""
        # Бір email бір реттен артық болмауы керек (DRY - тек бір жерде тексеру)
        if self._find_user_by_email(email):
            return f"Пайдаланушы '{email}' email-мен қазірдің өзінде бар"

        user = User(name, email, role)
        self.users.append(user)
        return f"Пайдаланушы '{name}' сәтті қосылды"

    def remove_user(self, email):
        """Пайдаланушыны жою (KISS - қарапайым әдіс)"""
        user = self._find_user_by_email(email)
        if user:
            self.users.remove(user)
            return f"Пайдаланушы '{email}' сәтті жойылды"
        return f"Пайдаланушы '{email}' табылмады"

    def update_user(self, email, new_name=None, new_role=None):
        """Пайдаланушыны жаңарту (DRY - бір әдісте барлық жаңарту операциялары)"""
        user = self._find_user_by_email(email)
        if not user:
            return f"Пайдаланушы '{email}' табылмады"

        # Тек берілген мәндерді жаңарту
        if new_name:
            old_name = user.name
            user.name = new_name

        if new_role:
            old_role = user.role
            user.role = new_role

        # Өзгерістер туралы хабарлама
        changes = []
        if new_name:
            changes.append(f"есімі '{old_name}' -> '{new_name}'")
        if new_role:
            changes.append(f"рөлі '{old_role}' -> '{new_role}'")

        if changes:
            return f"Пайдаланушы '{email}' сәтті жаңартылды: {', '.join(changes)}"
        return f"Пайдаланушы '{email}' жаңартылмады (өзгерістер жоқ)"

    def _find_user_by_email(self, email):
        """Пайдаланушыны email бойынша табу (DRY - бұл логиканы қайталамау)"""
        for user in self.users:
            if user.email == email:
                return user
        return None

    def show_all_users(self):
        """Барлық пайдаланушыларды көрсету (YAGNI - қазір қажетті функционал)"""
        if not self.users:
            return "Пайдаланушылар тізімі бос"

        result = "\n=== БАРЛЫҚ ПАЙДАЛАНУШЫЛАР ===\n"
        for i, user in enumerate(self.users, 1):
            result += f"{i}. {user}\n"

        result += f"\nБарлығы: {len(self.users)} пайдаланушы"
        return result


# ==============================
# БАСТАПҚЫ ТЕСТІЛЕУ ФУНКЦИЯЛАРЫ
# ==============================

def test_vehicle_system():
    """Көлік құралдарын басқару жүйесін тестілеу (Модуль 01)"""
    print("\n" + "=" * 60)
    print("МОДУЛЬ 01: КӨЛІК ҚҰРАЛДАРЫН БАСҚАРУ ЖҮЙЕСІ")
    print("=" * 60)

    # Көлік құралдарын құру
    print("\n1. КӨЛІК ҚҰРАЛДАРЫН ҚҰРУ:")
    car1 = Car("Toyota", "Camry", 2022, 4, "Автоматты")
    car2 = Car("Honda", "Civic", 2023, 4, "Механикалық")
    motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2021, "Классикалық", True)
    motorcycle2 = Motorcycle("Yamaha", "R1", 2023, "Спорттық", False)

    print(f"- {car1}")
    print(f"- {car2}")
    print(f"- {motorcycle1}")
    print(f"- {motorcycle2}")

    # Қозғалтқышты басқаруды тестілеу
    print("\n2. ҚОЗҒАЛТҚЫШТЫ БАСҚАРУ:")
    print(f"- {car1.start_engine()}")
    print(f"- {car1.start_engine()}")  # Қайталап іске қосу
    print(f"- {car1.stop_engine()}")
    print(f"- {motorcycle1.start_engine()}")

    # Гараждарды құру және көлік құралдарын қосу
    print("\n3. ГАРАЖДАРДЫ БАСҚАРУ:")
    garage1 = Garage("Орталық гараж")
    garage2 = Garage("Шығыс гараж")

    print(f"- {garage1.add_vehicle(car1)}")
    print(f"- {garage1.add_vehicle(car2)}")
    print(f"- {garage2.add_vehicle(motorcycle1)}")
    print(f"- {garage2.add_vehicle(motorcycle2)}")

    # Гараждарды көрсету
    print(garage1.show_vehicles())
    print(garage2.show_vehicles())

    # Автопаркты құру және басқару
    print("\n4. АВТОПАРКТЫ БАСҚАРУ:")
    fleet = Fleet("Негізгі автопарк")

    print(f"- {fleet.add_garage(garage1)}")
    print(f"- {fleet.add_garage(garage2)}")

    # Автопаркты көрсету
    print(fleet.show_all_vehicles())

    # Көлік құралын іздеу
    print("\n5. КӨЛІК ҚҰРАЛЫН ІЗДЕУ:")
    found_vehicles = fleet.find_vehicle("Toyota", "Camry")
    if found_vehicles:
        for vehicle, garage in found_vehicles:
            print(f"- Табылды: {vehicle} гаражда '{garage.name}'")
    else:
        print("- Көлік құралы табылмады")

    # Көлік құралын жою
    print("\n6. КӨЛІК ҚҰРАЛЫН ЖОЮ:")
    print(f"- {garage1.remove_vehicle('Toyota', 'Camry')}")
    print(f"- {garage1.remove_vehicle('Tesla', 'Model S')}")  # Жоқ көлік

    # Гараж жою
    print(f"\n- {fleet.remove_garage('Орталық гараж')}")

    # Соңғы жағдайды көрсету
    print("\n7. СОҢҒЫ ЖАҒДАЙ:")
    print(fleet.show_all_vehicles())


def test_user_system():
    """Пайдаланушыларды басқару жүйесін тестілеу (Модуль 02)"""
    print("\n" + "=" * 60)
    print("МОДУЛЬ 02: ПАЙДАЛАНУШЫЛАРДЫ БАСҚАРУ ЖҮЙЕСІ")
    print("(YAGNI, KISS, DRY ПРИНЦИПТЕРІН ҚОЛДАНУ)")
    print("=" * 60)

    # UserManager құру
    user_manager = UserManager()

    # Пайдаланушыларды қосу
    print("\n1. ПАЙДАЛАНУШЫЛАРДЫ ҚОСУ:")
    print(f"- {user_manager.add_user('Айгерім Сәтбаева', 'aigerim@company.kz', 'Admin')}")
    print(f"- {user_manager.add_user('Нұрлан Жақыпов', 'nurlan@company.kz', 'User')}")
    print(f"- {user_manager.add_user('Мәдина Қасенова', 'madina@company.kz')}")  # Рөлсіз (әдепкі 'User')
    print(f"- {user_manager.add_user('Нұрлан Жақыпов', 'nurlan@company.kz', 'User')}")  # Қайталау

    # Барлық пайдаланушыларды көрсету
    print(user_manager.show_all_users())

    # Пайдаланушыны жаңарту
    print("\n2. ПАЙДАЛАНУШЫНЫ ЖАҢАРТУ:")
    print(f"- {user_manager.update_user('nurlan@company.kz', new_name='Нұрлан Жаңаев')}")
    print(f"- {user_manager.update_user('madina@company.kz', new_role='Manager')}")
    print(f"- {user_manager.update_user('aigerim@company.kz', new_name='Айгерім Жаңаева', new_role='Super Admin')}")
    print(f"- {user_manager.update_user('жоқ@company.kz')}")  # Жоқ пайдаланушы

    # Жаңартылған тізімді көрсету
    print(user_manager.show_all_users())

    # Пайдаланушыны жою
    print("\n3. ПАЙДАЛАНУШЫНЫ ЖОЮ:")
    print(f"- {user_manager.remove_user('madina@company.kz')}")
    print(f"- {user_manager.remove_user('жоқ@company.kz')}")  # Жоқ пайдаланушы

    # Соңғы тізімді көрсету
    print(user_manager.show_all_users())

    # Принциптерді түсіндіру
    print("\n4. ҚОЛДАНЫЛҒАН ПРИНЦИПТЕР:")
    print("""YAGNI (You Ain't Gonna Need It):
  - Тек қажетті функционалдық: қосу, жою, жаңарту
  - Қосымша іздеу, сұрыптау әдістері жоқ

KISS (Keep It Simple, Stupid):
  - Қарапайым кластар және әдістер
  - Күрделі мұрагерлік немесе интерфейстер жоқ
  - Минималды тексерулер

DRY (Don't Repeat Yourself):
  - Бірыңғай пайдаланушы табу әдісі (_find_user_by_email)
  - Жаңарту әдісінде барлық өзгерістер бір жерде
  - Ортақ логикаларды қайталамау""")


# ==============================
# БАСҚАРУ БӨЛІМІ
# ==============================

def main():
    """Басты функция - барлық жүйелерді іске қосады"""
    print("=" * 70)
    print("ШАБЛОНДАРДЫ ЖОБАЛАУ ПРАКТИКАЛЫҚ ЖҰМЫСТАРЫ")
    print("=" * 70)
    print("Бұл бағдарлама екі практикалық жұмысты қамтиды:")
    print("1. Модуль 01 - Көлік құралдарын басқару жүйесі")
    print("2. Модуль 02 - Пайдаланушыларды басқару жүйесі")
    print("=" * 70)

    # Модуль 01: Көлік құралдарын басқару жүйесі
    test_vehicle_system()

    # Модуль 02: Пайдаланушыларды басқару жүйесі
    test_user_system()

    print("\n" + "=" * 70)
    print("БАРЛЫҚ ТЕСТІЛЕУ АЯҚТАЛДЫ!")
    print("=" * 70)


# Бағдарламаны іске қосу
if __name__ == "__main__":
    main()