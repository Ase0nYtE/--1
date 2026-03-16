from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

class IReport(ABC):
    @abstractmethod
    def generate(self) -> str:
        pass

class SalesReport(IReport):
    def __init__(self):
        self.sales = [
            {"id": 1, "date": "2025-03-01", "amount": 4500, "user": "Aset"},
            {"id": 2, "date": "2025-03-05", "amount": 12000, "user": "Aidar"},
            {"id": 3, "date": "2025-03-10", "amount": 7800, "user": "Aset"},
            {"id": 4, "date": "2025-03-15", "amount": 3200, "user": "Dina"},
        ]

    def generate(self) -> str:
        lines = ["Отчёт по продажам\n"]
        for s in self.sales:
            lines.append(f"{s['date']} | {s['user']} | {s['amount']} ₸")
        return "\n".join(lines)

class UserReport(IReport):
    def __init__(self):
        self.users = [
            {"name": "Aset", "orders": 12, "total": 45800},
            {"name": "Aidar", "orders": 5, "total": 32000},
            {"name": "Dina", "orders": 8, "total": 21500},
        ]

    def generate(self) -> str:
        lines = ["Отчёт по пользователям\n"]
        for u in self.users:
            lines.append(f"{u['name']} | заказов: {u['orders']} | сумма: {u['total']} ₸")
        return "\n".join(lines)

class ReportDecorator(IReport):
    def __init__(self, report: IReport):
        self._report = report

    def generate(self) -> str:
        return self._report.generate()

class DateFilterDecorator(ReportDecorator):
    def __init__(self, report: IReport, start_date: str, end_date: str):
        super().__init__(report)
        self.start = datetime.strptime(start_date, "%Y-%m-%d")
        self.end = datetime.strptime(end_date, "%Y-%m-%d")

    def generate(self) -> str:
        base = self._report.generate()
        if "Отчёт по продажам" not in base:
            return base + "\n(фильтр по датам применяется только к продажам)"

        lines = base.split("\n")
        result = [lines[0]]
        for line in lines[1:]:
            if not line.strip():
                continue
            date_str = line.split(" | ")[0]
            date = datetime.strptime(date_str, "%Y-%m-%d")
            if self.start <= date <= self.end:
                result.append(line)
        return "\n".join(result)

class SortingDecorator(ReportDecorator):
    def __init__(self, report: IReport, by: str = "amount"):
        super().__init__(report)
        self.by = by

    def generate(self) -> str:
        base = self._report.generate()
        if "Отчёт по продажам" in base:
            header = base.split("\n")[0]
            data_lines = base.split("\n")[1:]
            data = []
            for line in data_lines:
                if line.strip():
                    parts = line.split(" | ")
                    data.append((parts[0], parts[1], float(parts[2].replace(" ₸", ""))))
            if self.by == "amount":
                data.sort(key=lambda x: x[2], reverse=True)
            elif self.by == "date":
                data.sort(key=lambda x: x[0])
            sorted_lines = [f"{d[0]} | {d[1]} | {d[2]} ₸" for d in data]
            return header + "\n" + "\n".join(sorted_lines)
        return base

class CsvExportDecorator(ReportDecorator):
    def generate(self) -> str:
        base = self._report.generate()
        lines = base.split("\n")
        csv_lines = []
        for line in lines:
            csv_lines.append(line.replace(" | ", ","))
        return "\n".join(csv_lines) + "\n(готово к сохранению в CSV)"

class PdfExportDecorator(ReportDecorator):
    def generate(self) -> str:
        base = self._report.generate()
        return base + "\n\n(экспортировано в PDF-формат с красивым оформлением)"

if __name__ == "__main__":
    print("=== Базовый отчёт по продажам ===")
    report = SalesReport()
    print(report.generate())

    print("\n=== Отчёт по продажам + фильтр по датам (01.03–10.03) ===")
    filtered = DateFilterDecorator(report, "2025-03-01", "2025-03-10")
    print(filtered.generate())

    print("\n=== Отчёт по продажам + сортировка по сумме + CSV ===")
    sorted_csv = CsvExportDecorator(SortingDecorator(report, by="amount"))
    print(sorted_csv.generate())

    print("\n=== Отчёт по пользователям + PDF ===")
    pdf_users = PdfExportDecorator(UserReport())
    print(pdf_users.generate())