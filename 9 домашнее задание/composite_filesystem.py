from abc import ABC, abstractmethod
from typing import List

class FileSystemComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, level: int = 0):
        pass


class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def display(self, level: int = 0):
        indent = "  " * level
        print(f"{indent}├─ 📄 {self.name} ({self.size} bytes)")


class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        if component not in self.children:
            self.children.append(component)

    def remove(self, component: FileSystemComponent):
        if component in self.children:
            self.children.remove(component)

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)

    def display(self, level: int = 0):
        indent = "  " * level
        print(f"{indent}└─ 📁 {self.name} (size: {self.get_size()} bytes)")
        for child in self.children:
            child.display(level + 1)


if __name__ == "__main__":
    root = Directory("Root")

    documents = Directory("Documents")
    images = Directory("Images")
    videos = Directory("Videos")

    root.add(documents)
    root.add(images)
    root.add(videos)

    documents.add(File("report.pdf", 2450000))
    documents.add(File("contract.docx", 890000))

    images.add(File("photo1.jpg", 3200000))
    images.add(File("photo2.png", 1850000))

    videos.add(File("movie.mp4", 1250000000))
    videos.add(File("tutorial.mkv", 850000000))

    work = Directory("Work Files")
    documents.add(work)
    work.add(File("presentation.pptx", 5400000))
    work.add(File("budget.xlsx", 670000))

    print("=== File System Structure ===\n")
    root.display()

    print("\n=== Summary ===")
    print(f"Total size: {root.get_size():,} bytes")