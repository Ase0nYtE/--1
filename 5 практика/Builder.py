from abc import ABC, abstractmethod

class ReportStyle:
    def __init__(self, bg_color: str = "white", font_color: str = "black", font_size: int = 12):
        self.bg_color = bg_color
        self.font_color = font_color
        self.font_size = font_size

class Report:
    def __init__(self):
        self.header: str = ""
        self.content: str = ""
        self.footer: str = ""
        self.style: ReportStyle = ReportStyle()

    def export(self, format: str):
        print(f"Export to {format}:")
        print(f"Style: background {self.style.bg_color}, font {self.style.font_color} ({self.style.font_size}pt)")
        print(self.header)
        print(self.content)
        print(self.footer)

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
    def set_style(self, style: ReportStyle) -> 'IReportBuilder':
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

    def set_style(self, style: ReportStyle) -> 'IReportBuilder':
        self.report.style = style
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

    def set_style(self, style: ReportStyle) -> 'IReportBuilder':
        self.report.style = style
        return self

    def get_report(self) -> Report:
        return self.report

class PdfReportBuilder(IReportBuilder):  # Placeholder, without real library
    def __init__(self):
        self.report = Report()

    def set_header(self, header: str) -> 'IReportBuilder':
        self.report.header = f"PDF Header: {header}"
        return self

    def set_content(self, content: str) -> 'IReportBuilder':
        self.report.content = f"PDF Content: {content}"
        return self

    def set_footer(self, footer: str) -> 'IReportBuilder':
        self.report.footer = f"PDF Footer: {footer}"
        return self

    def set_style(self, style: ReportStyle) -> 'IReportBuilder':
        self.report.style = style
        return self

    def get_report(self) -> Report:
        return self.report

class ReportDirector:
    @staticmethod
    def construct_report(builder: IReportBuilder, style: ReportStyle) -> Report:
        return (builder
                .set_style(style)
                .set_header("Report")
                .set_content("Content")
                .set_footer("Footer")
                .get_report())

if __name__ == "__main__":
    style = ReportStyle("gray", "blue", 14)

    text_builder = TextReportBuilder()
    text_report = ReportDirector.construct_report(text_builder, style)
    text_report.export("Text")

    pdf_builder = PdfReportBuilder()
    pdf_report = ReportDirector.construct_report(pdf_builder, style)
    pdf_report.export("PDF")