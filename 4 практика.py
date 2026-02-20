from abc import ABC, abstractmethod
from typing import Optional


class Document(ABC):
    @abstractmethod
    def open(self) -> None:
        pass


class Report(Document):
    def open(self) -> None:
        print("Opened document: Report → viewing analytics and charts")


class Resume(Document):
    def open(self) -> None:
        print("Opened resume → displaying experience, skills, education")


class Letter(Document):
    def open(self) -> None:
        print("Opened letter → displaying subject, recipient, body")


class Invoice(Document):
    def open(self) -> None:
        print("Opened invoice → displaying amount, items, payment details")


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass


class ReportCreator(DocumentCreator):
    def create_document(self) -> Document:
        return Report()


class ResumeCreator(DocumentCreator):
    def create_document(self) -> Document:
        return Resume()


class LetterCreator(DocumentCreator):
    def create_document(self) -> Document:
        return Letter()


class InvoiceCreator(DocumentCreator):
    def create_document(self) -> Document:
        return Invoice()


def main():
    creators = {
        "1": ("Report", ReportCreator()),
        "2": ("Resume", ResumeCreator()),
        "3": ("Letter", LetterCreator()),
        "4": ("Invoice", InvoiceCreator()),
    }

    print("Available document types:")
    for key, (name, _) in creators.items():
        print(f"  {key}) {name}")

    choice = input("\nSelect document type (1–4): ").strip()

    if choice not in creators:
        print("Invalid choice.")
        return

    name, factory = creators[choice]
    print(f"\nCreating: {name}")
    document = factory.create_document()
    document.open()


if __name__ == "__main__":
    main()