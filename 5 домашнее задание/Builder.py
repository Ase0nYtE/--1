from abc import ABC, abstractmethod
from typing import List

class Report:
    def __init__(self):
        self.header: str = ""
        self.content: str = ""
        self.footer: str = ""

    def show(self):
        print("=" * 50)
        if self.header:
            print(self.header.center(50))
            print("-" * 50)
        if self.content:
            print(self.content)
        if self.footer:
            print("-" * 50)
            print(self.footer.center(50))
        print("=" * 50)

class IReportBuilder(ABC):
    @abstractmethod
    def set_header(self, header: str) -> 'IReportBuilder':
        pass

    @abstractmethod
    def set_content(self, content: str) -> 'IReportBuilder':
        pass

    @abstractmethod
    def set_footer(self, footer: str) -> 'IReportBuilder':
        pass

    @abstractmethod
    def get_report(self) -> Report:
        pass

class TextReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header: str) -> 'IReportBuilder':
        self.report.header = header
        return self

    def set_content(self, content: str) -> 'IReportBuilder':
        self.report.content = content
        return self

    def set_footer(self, footer: str) -> 'IReportBuilder':
        self.report.footer = footer
        return self

    def get_report(self) -> Report:
        return self.report

class HtmlReportBuilder(IReportBuilder):
    def __init__(self):
        self.report = Report()

    def set_header(self, header: str) -> 'IReportBuilder':
        self.report.header = f"<h1>{header}</h1>"
        return self

    def set_content(self, content: str) -> 'IReportBuilder':
        self.report.content = f"<p>{content}</p>"
        return self

    def set_footer(self, footer: str) -> 'IReportBuilder':
        self.report.footer = f"<small>{footer}</small>"
        return self

    def get_report(self) -> Report:
        return self.report

class ReportDirector:
    @staticmethod
    def construct_simple_report(builder: IReportBuilder) -> Report:
        return (builder
                .set_header("Monthly Report")
                .set_content("Main content here...")
                .set_footer("© 2026 Company")
                .get_report())

if __name__ == "__main__":
    text_builder = TextReportBuilder()
    text_report = ReportDirector.construct_simple_report(text_builder)
    text_report.show()

    html_builder = HtmlReportBuilder()
    html_report = ReportDirector.construct_simple_report(html_builder)
    html_report.show()