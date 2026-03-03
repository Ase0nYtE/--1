from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    def generate_report(self):
        self.collect_data()
        self.format_data()
        self.generate_header()
        self.generate_body()
        self.generate_footer()
        if self.customer_wants_save():
            self.save_report()

    def collect_data(self):
        print("Сбор данных...")

    def format_data(self):
        print("Форматирование данных...")

    def generate_header(self):
        print("Генерация заголовка отчёта")

    @abstractmethod
    def generate_body(self):
        pass

    def generate_footer(self):
        print("Генерация подвала отчёта")

    def customer_wants_save(self) -> bool:
        return True

    def save_report(self):
        print("Отчёт сохранён")

class PdfReport(ReportGenerator):
    def generate_body(self):
        print("Создание PDF-содержимого")

class ExcelReport(ReportGenerator):
    def generate_body(self):
        print("Создание таблицы Excel")

    def save_report(self):
        print("Excel-файл сохранён (.xlsx)")

class HtmlReport(ReportGenerator):
    def generate_body(self):
        print("Генерация HTML-разметки")

    def customer_wants_save(self) -> bool:
        return input("Сохранить HTML? (y/n): ").lower() == 'y'

if __name__ == "__main__":
    print("PDF отчёт:")
    PdfReport().generate_report()

    print("\nExcel отчёт:")
    ExcelReport().generate_report()

    print("\nHTML отчёт:")
    HtmlReport().generate_report()