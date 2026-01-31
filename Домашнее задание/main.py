# main.py
class Book:
    """Кітапхана жүйесіндегі кітапты білдіреді"""

    def __init__(self, title, author, isbn, copies_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def __str__(self):
        return f"{self.title} ({self.author}), ISBN: {self.isbn} - {self.copies_available} дана қолжетімді"


class Reader:
    """Кітапхана оқырманын білдіреді"""

    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id

    def __str__(self):
        return f"{self.name} (ID: {self.reader_id})"


class Library:
    """Кітаптарды, оқырмандарды және кітап беру операцияларын басқарады"""

    def __init__(self):
        self.books = []
        self.readers = []

    def add_book(self, book):
        """Кітапханаға жаңа кітап қосу"""
        self.books.append(book)
        print(f"Кітап қосылды: {book.title}")

    def remove_book(self, isbn):
        """ISBN бойынша кітапты жою"""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Кітап жойылды: {book.title}")
                return
        print(f"ISBN {isbn} бар кітап табылмады")

    def register_reader(self, reader):
        """Жаңа оқырманды тіркеу"""
        self.readers.append(reader)
        print(f"Оқырман тіркелді: {reader.name}")

    def remove_reader(self, reader_id):
        """ID бойынша оқырманды жою"""
        for reader in self.readers:
            if reader.reader_id == reader_id:
                self.readers.remove(reader)
                print(f"Оқырман жойылды: {reader.name}")
                return
        print(f"ID {reader_id} бар оқырман табылмады")

    def lend_book(self, isbn, reader_id):
        """Қолжетімді болса, оқырманға кітап беру"""
        book = next((b for b in self.books if b.isbn == isbn), None)
        reader = next((r for r in self.readers if r.reader_id == reader_id), None)

        if not book:
            print(f"ISBN {isbn} бар кітап табылмады")
            return
        if not reader:
            print(f"ID {reader_id} бар оқырман табылмады")
            return
        if book.copies_available <= 0:
            print(f"'{book.title}' кітабының қолжетімді даналары жоқ")
            return

        book.copies_available -= 1
        print(f"Кітап '{book.title}' {reader.name} оқырманына берілді")

    def return_book(self, isbn):
        """Кітапты кітапханаға қайтару"""
        book = next((b for b in self.books if b.isbn == isbn), None)
        if book:
            book.copies_available += 1
            print(f"Кітап '{book.title}' қайтарылды")
        else:
            print(f"ISBN {isbn} бар кітап табылмады")

    def show_all_books(self):
        """Барлық кітаптарды көрсету"""
        if not self.books:
            print("Кітаптар тізімі бос")
            return
        print("\n=== БАРЛЫҚ КІТАПТАР ===")
        for book in self.books:
            print(f"- {book}")

    def show_all_readers(self):
        """Барлық оқырмандарды көрсету"""
        if not self.readers:
            print("Оқырмандар тізімі бос")
            return
        print("\n=== БАРЛЫҚ ОҚЫРМАНДАР ===")
        for reader in self.readers:
            print(f"- {reader}")


# ==============================
# МОДУЛЬ 02: DRY, KISS, YAGNI ПРИНЦИПТЕРІ
# ==============================

# DRY принципі (Қайталанбау)
class Logger:
    """Журналдау әдістерін біріктіреді"""

    @staticmethod
    def log(level, message):
        """Журналдаудың параметрленген әдісі"""
        print(f"{level}: {message}")


class Configuration:
    """Ортақ конфигурациялық параметрлер"""
    CONNECTION_STRING = "Server=myServer;Database=myDb;User Id=myUser;Password=myPass;"


class DatabaseService:
    """Дерекқор қызметі"""

    def connect(self):
        connection_string = Configuration.CONNECTION_STRING
        # Дерекқорға қосылу логикасы
        print("Дерекқорға қосылу...")


class LoggingService:
    """Журналдау қызметі"""

    def log_to_db(self, message):
        connection_string = Configuration.CONNECTION_STRING
        # Дерекқорға журнал жазу логикасы
        print(f"Дерекқорға журнал жазылуда: {message}")


# KISS принципі (Қарапайым болу)
class SimpleProcessor:
    """Қажетсіз кірістірулерсіз қарапайым әдістер"""

    @staticmethod
    def process_numbers(numbers):
        """Сандарды өңдеу - қажетсіз кірістірулерсіз"""
        if not numbers:
            return

        for number in numbers:
            if number > 0:
                print(number)

    @staticmethod
    def print_positive_numbers(numbers):
        """Оң сандарды шығару - қажетсіз LINQ қолданбай"""
        for number in numbers:
            if number > 0:
                print(number)

    @staticmethod
    def divide(a, b):
        """Бөлу операциясы - артық ерекше жағдайларды қолданбай"""
        if b == 0:
            return 0
        return a / b


# YAGNI принципі (Қажет емес нәрселерді қоспау)
class User:
    """Пайдаланушы класы - тек қажетті қасиеттермен"""

    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    """Пайдаланушыны сақтауға арналған бөлек класс"""

    def save(self, user):
        # Пайдаланушыны дерекқорға сақтау
        print(f"{user.name} дерекқорға сақталды")


class FileReader:
    """Файлды оқу - қажетсіз параметрлерсіз"""

    def read_file(self, file_path):
        # Қарапайым файл оқу логикасы
        return "файл мазмұны"


class ReportGenerator:
    """Есептерді генерациялау - қазір қажет әдістер ғана"""

    def generate_pdf_report(self):
        # PDF есепті генерациялау
        print("PDF есеп генерацияланды")


# ==============================
# БАСТАПҚЫ ТЕСТІЛЕУ КОДЫ
# ==============================

def test_library_system():
    """Кітапхана жүйесін тестілеу"""
    print("=== КІТАПХАНА ЖҮЙЕСІН ТЕСТІЛЕУ ===")

    library = Library()

    # Кітаптарды құру
    book1 = Book("Ұлы Гэтсби", "Ф. Скотт Фицджеральд", "123456", 5)
    book2 = Book("1984", "Джордж Оруэлл", "789012", 3)
    book3 = Book("Көкпек", "Шерхан Мұртаза", "345678", 2)

    # Оқырмандарды құру
    reader1 = Reader("Әлия Жансүгірова", 101)
    reader2 = Reader("Бахытжан Серік", 102)

    # Кітаптарды қосу
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Оқырмандарды тіркеу
    library.register_reader(reader1)
    library.register_reader(reader2)

    # Барлық кітаптар мен оқырмандарды көрсету
    library.show_all_books()
    library.show_all_readers()

    # Кітап беруді тестілеу
    print("\n=== КІТАП БЕРУ ТЕСТІ ===")
    library.lend_book("123456", 101)
    library.lend_book("789012", 102)
    library.lend_book("123456", 101)  # Тағы бір дана

    # Кітап қайтаруды тестілеу
    print("\n=== КІТАП ҚАЙТАРУ ТЕСТІ ===")
    library.return_book("123456")

    # Кітаптарды көрсету (даналар саны өзгергенін тексеру)
    library.show_all_books()

    # Жою операцияларын тестілеу
    print("\n=== ЖОЮ ОПЕРАЦИЯЛАРЫ ===")
    library.remove_book("789012")
    library.remove_reader(102)

    # Соңғы жағдайды көрсету
    library.show_all_books()
    library.show_all_readers()


def test_design_principles():
    """Жобалау принциптерін тестілеу"""
    print("\n\n=== ЖОБАЛАУ ПРИНЦИПТЕРІН ТЕСТІЛЕУ ===")

    # DRY принципін тестілеу
    print("\n1. DRY ПРИНЦИПІ:")
    logger = Logger()
    logger.log("ҚАТЕ", "Бұл қате хабарламасы")
    logger.log("ЕСКЕРТУ", "Бұл ескерту хабарламасы")
    logger.log("АҚПАРАТ", "Бұл ақпараттық хабарлама")

    # KISS принципін тестілеу
    print("\n2. KISS ПРИНЦИПІ:")
    processor = SimpleProcessor()
    numbers = [5, -2, 10, -8, 3]

    print("Оң сандар:")
    processor.process_numbers(numbers)

    print("Бөлу нәтижесі (10 / 2):", processor.divide(10, 2))
    print("Бөлу нәтижесі (10 / 0):", processor.divide(10, 0))

    # YAGNI принципін тестілеу
    print("\n3. YAGNI ПРИНЦИПІ:")
    user = User("Нұрлан Сапаров", "nurlan@example.com")
    user_repo = UserRepository()
    user_repo.save(user)

    file_reader = FileReader()
    print("Оқылған файл:", file_reader.read_file("test.txt"))

    report_gen = ReportGenerator()
    report_gen.generate_pdf_report()


# ==============================
# БАСҚАРУ БӨЛІМІ
# ==============================

if __name__ == "__main__":
    print("=" * 50)
    print("БҰЛ КОД ЕКІ МОДУЛЬДІ ҚАМТИДЫ:")
    print("1. МОДУЛЬ 01 - КІТАПХАНА БАСҚАРУ ЖҮЙЕСІ")
    print("2. МОДУЛЬ 02 - DRY, KISS, YAGNI ПРИНЦИПТЕРІ")
    print("=" * 50)

    # Кітапхана жүйесін тестілеу
    test_library_system()

    # Жобалау принциптерін тестілеу
    test_design_principles()

    print("\n" + "=" * 50)
    print("БАРЛЫҚ ТЕСТІЛЕУ АЯҚТАЛДЫ!")
    print("=" * 50)