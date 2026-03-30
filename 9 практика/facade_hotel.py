class RoomBookingSystem:
    def book_room(self, room_number: str, guest: str, days: int) -> str:
        return f"Номер {room_number} забронирован для {guest} на {days} дней"

    def cancel_room(self, room_number: str) -> str:
        return f"Бронирование номера {room_number} отменено"

    def check_availability(self, room_number: str) -> bool:
        return True


class RestaurantSystem:
    def book_table(self, table_number: int, guest: str, time: str) -> str:
        return f"Стол №{table_number} забронирован для {guest} на {time}"

    def order_food(self, guest: str, dishes: list) -> str:
        return f"Заказ для {guest}: {', '.join(dishes)} принят"


class EventManagementSystem:
    def book_hall(self, hall_name: str, event_name: str, date: str) -> str:
        return f"Зал '{hall_name}' забронирован для '{event_name}' на {date}"

    def order_equipment(self, equipment: list) -> str:
        return f"Оборудование заказано: {', '.join(equipment)}"


class CleaningService:
    def schedule_cleaning(self, room_number: str, time: str) -> str:
        return f"Уборка номера {room_number} запланирована на {time}"

    def perform_cleaning(self, room_number: str) -> str:
        return f"Уборка номера {room_number} выполнена"


class HotelFacade:
    def __init__(self):
        self.rooms = RoomBookingSystem()
        self.restaurant = RestaurantSystem()
        self.events = EventManagementSystem()
        self.cleaning = CleaningService()

    def book_room_with_services(self, room_number: str, guest: str, days: int, dishes: list = None):
        print(self.rooms.book_room(room_number, guest, days))

        if dishes:
            print(self.restaurant.order_food(guest, dishes))

        print(self.cleaning.schedule_cleaning(room_number, "завтра 10:00"))
        print("Комплексное бронирование номера завершено.\n")

    def organize_event(self, event_name: str, hall: str, date: str, participants: int, equipment: list):
        print(self.events.book_hall(hall, event_name, date))
        print(f"Забронировано {participants} номеров для участников")
        print(self.events.order_equipment(equipment))
        print("Мероприятие успешно организовано.\n")

    def book_table_with_taxi(self, table_number: int, guest: str, time: str):
        print(self.restaurant.book_table(table_number, guest, time))
        print("Такси заказано к ресторану на указанное время")
        print("Бронирование стола с такси завершено.\n")

    def cancel_booking(self, room_number: str):
        print(self.rooms.cancel_room(room_number))
        print("Бронирование успешно отменено.\n")


if __name__ == "__main__":
    hotel = HotelFacade()

    print("=== Бронирование номера с услугами ===")
    hotel.book_room_with_services("305", "Асет", 3, ["Плов", "Салат", "Чай"])

    print("=== Организация мероприятия ===")
    hotel.organize_event("Корпоратив", "Конференц-зал A", "2025-04-15", 25,
                         ["Проектор", "Звук", "Микрофоны"])

    print("=== Бронирование стола в ресторане ===")
    hotel.book_table_with_taxi(12, "Айдар", "19:30")

    print("=== Отмена бронирования ===")
    hotel.cancel_booking("305")