# homework_solid_principles.py
from abc import ABC, abstractmethod
from typing import List


class Tapsyrys:
    def __init__(self):
        self.onim_aty: str = ""
        self.sany: int = 0
        self.bagasy: float = 0.0

    def __repr__(self):
        return f"Tapsyrys({self.onim_aty}, {self.sany} × {self.bagasy})"


class BaganyEsepteu:
    @staticmethod
    def jalpy_bagany_esepteu(tapsyrys: Tapsyrys) -> float:
        return tapsyrys.sany * tapsyrys.bagasy * 0.9


class TolemProcessor:
    @staticmethod
    def tolem_jasau(tolem_turaly: str) -> None:
        print(f"Төлем өңделді: {tolem_turaly}")


class EmailHabarlandyru:
    @staticmethod
    def rastau_haty_jiberu(email: str) -> None:
        print(f"Растау хаты {email} мекенжайына жіберілді")


# 2. Open-Closed Principle (OCP)

class Qyzmetker:
    def __init__(self, aty: str, negizgi_zhalaqy: float, tip: str):
        self.aty = aty
        self.negizgi_zhalaqy = negizgi_zhalaqy
        self.tip = tip


class ZhalaqyEsepteu(ABC):
    @abstractmethod
    def esepteu(self, qyzmetker: Qyzmetker) -> float:
        pass


class TuraqtyZhalaqy(ZhalaqyEsepteu):
    def esepteu(self, qyzmetker: Qyzmetker) -> float:
        return qyzmetker.negizgi_zhalaqy * 1.20


class KelisimshartZhalaqy(ZhalaqyEsepteu):
    def esepteu(self, qyzmetker: Qyzmetker) -> float:
        return qyzmetker.negizgi_zhalaqy * 1.10


class StazherZhalaqy(ZhalaqyEsepteu):
    def esepteu(self, qyzmetker: Qyzmetker) -> float:
        return qyzmetker.negizgi_zhalaqy * 0.80


class FreelancerZhalaqy(ZhalaqyEsepteu):
    def esepteu(self, qyzmetker: Qyzmetker) -> float:
        return qyzmetker.negizgi_zhalaqy * 1.05


# 3. Interface Segregation Principle (ISP)

class Printer(ABC):
    @abstractmethod
    def basyp_shygaru(self, mazmun: str) -> None:
        pass


class Skaner(ABC):
    @abstractmethod
    def skanirleu(self, mazmun: str) -> None:
        pass


class Fax(ABC):
    @abstractmethod
    def fax_jiberu(self, mazmun: str) -> None:
        pass


class BarlyqBirdeyPrinter(Printer, Skaner, Fax):
    def basyp_shygaru(self, mazmun: str) -> None:
        print(f"[Басу] {mazmun}")

    def skanirleu(self, mazmun: str) -> None:
        print(f"[Сканерлеу] {mazmun}")

    def fax_jiberu(self, mazmun: str) -> None:
        print(f"[Факс] {mazmun}")


class QarapaiymPrinter(Printer):
    def basyp_shygaru(self, mazmun: str) -> None:
        print(f"[Басу] {mazmun}")


# 4. Dependency Inversion Principle (DIP)

class HabarJiberu(ABC):
    @abstractmethod
    def zhiberu(self, habar: str) -> None:
        pass


class EmailJiberu(HabarJiberu):
    def zhiberu(self, habar: str) -> None:
        print(f"[Email] → {habar}")


class SmsJiberu(HabarJiberu):
    def zhiberu(self, habar: str) -> None:
        print(f"[SMS] → {habar}")


class HabarlandyruQyzmeti:
    def __init__(self, jiberushiler: List[HabarJiberu]):
        self.jiberushiler = jiberushiler

    def habarlandyru(self, habar: str) -> None:
        for jiberushi in self.jiberushiler:
            jiberushi.zhiberu(habar)