# practice_online_duken.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Onim:
    aty: str
    bagasy: float


@dataclass
class TapsyrysElementi:
    onim: Onim
    sany: int

    @property
    def zhartysy(self) -> float:
        return self.onim.bagasy * self.sany


class Tapsyrys:
    def __init__(self, satyp_alushy_email: str = "", satyp_alushy_telefon: str = ""):
        self.elementter: List[TapsyrysElementi] = []
        self.tolem_tasi: Optional["Tolem"] = None
        self.zhetkizu_tasi: Optional["Zhetkizu"] = None
        self.satyp_alushy_email = satyp_alushy_email
        self.satyp_alushy_telefon = satyp_alushy_telefon

    def onim_qosu(self, onim: Onim, sany: int) -> None:
        self.elementter.append(TapsyrysElementi(onim, sany))

    @property
    def jalpy_soma(self) -> float:
        return sum(el.zhartysy for el in self.elementter)

    def tolem_tasin_tandau(self, tolem: "Tolem") -> None:
        self.tolem_tasi = tolem

    def zhetkizu_tasin_tandau(self, zhetkizu: "Zhetkizu") -> None:
        self.zhetkizu_tasi = zhetkizu


class Tolem(ABC):
    @abstractmethod
    def oryndau(self, soma: float) -> bool:
        pass

    @abstractmethod
    def sipattamasy(self) -> str:
        pass


class KartamenTolem(Tolem):
    def oryndau(self, soma: float) -> bool:
        print(f"[Карта] {soma:,.0f} теңге төлем өңделді")
        return True

    def sipattamasy(self) -> str:
        return "Банк картасы"


class PayPalTolem(Tolem):
    def oryndau(self, soma: float) -> bool:
        print(f"[PayPal] {soma:,.0f} теңге төлем өңделді")
        return True

    def sipattamasy(self) -> str:
        return "PayPal"


class ZhyldamTusiruIndirim(ABC):
    @abstractmethod
    def qoldanu(self, soma: float) -> float:
        pass


class Indirimsiz(ZhyldamTusiruIndirim):
    def qoldanu(self, soma: float) -> float:
        return soma


class PaizIndirim(ZhyldamTusiruIndirim):
    def __init__(self, paiz: float):
        self.paiz = paiz

    def qoldanu(self, soma: float) -> float:
        return soma * (1 - self.paiz / 100)


class TuraqtyIndirim(ZhyldamTusiruIndirim):
    def __init__(self, soma: float):
        self.soma = soma

    def qoldanu(self, soma: float) -> float:
        return max(0, soma - self.soma)


class IndirimEsepteu:
    def __init__(self):
        self.ereje: List[ZhyldamTusiruIndirim] = []

    def ereje_qosu(self, ereje: ZhyldamTusiruIndirim) -> None:
        self.ereje.append(ereje)

    def esepteu(self, bastapqy_soma: float) -> float:
        soma = bastapqy_soma
        for er in self.ereje:
            soma = er.qoldanu(soma)
        return soma


class Zhetkizu(ABC):
    @abstractmethod
    def zhetkizu(self, tapsyrys: Tapsyrys) -> None:
        pass

    @abstractmethod
    def sipattamasy(self) -> str:
        pass


class KurerZhetkizu(Zhetkizu):
    def zhetkizu(self, tapsyrys: Tapsyrys) -> None:
        print("[Курьер] Тапсырыс мекенжайға жеткізіледі")

    def sipattamasy(self) -> str:
        return "Курьер арқылы жеткізу"


class PunktidenAlu(Zhetkizu):
    def zhetkizu(self, tapsyrys: Tapsyrys) -> None:
        print("[ПВЗ] Тапсырыс беру пунктінде дайын")

    def sipattamasy(self) -> str:
        return "Өздігінен алып кету"


class Habarlandyru(ABC):
    @abstractmethod
    def zhiberu(self, habar: str) -> None:
        pass


class EmailHabarlandyru(Habarlandyru):
    def __init__(self, email: str):
        self.email = email

    def zhiberu(self, habar: str) -> None:
        print(f"[Email → {self.email}] {habar}")


class SmsHabarlandyru(Habarlandyru):
    def __init__(self, telefon: str):
        self.telefon = telefon

    def zhiberu(self, habar: str) -> None:
        print(f"[SMS → {self.telefon}] {habar}")


class TapsyrysQyzmeti:
    def __init__(self, indirim_esepteu: IndirimEsepteu, habarlandyrushylar: List[Habarlandyru]):
        self.indirim_esepteu = indirim_esepteu
        self.habarlandyrushylar = habarlandyrushylar

    def tapsyrys_ornyndau(self, tapsyrys: Tapsyrys) -> None:
        if not tapsyrys.elementter:
            print("Қате: тапсырыста тауар жоқ")
            return

        if not tapsyrys.tolem_tasi:
            print("Қате: төлем тәсілі таңдалмаған")
            return

        if not tapsyrys.zhetkizu_tasi:
            print("Қате: жеткізу тәсілі таңдалмаған")
            return

        soңgy_baga = self.indirim_esepteu.esepteu(tapsyrys.jalpy_soma)

        tabysty = tapsyrys.tolem_tasi.oryndau(soңgy_baga)
        if not tabysty:
            print("Төлем кезінде қате кетті")
            return

        tapsyrys.zhetkizu_tasi.zhetkizu(tapsyrys)

        habar = (
            f"Тапсырыс {soңgy_baga:,.0f} теңгеге төленді\n"
            f"Төлем: {tapsyrys.tolem_tasi.sipattamasy()}\n"
            f"Жеткізу: {tapsyrys.zhetkizu_tasi.sipattamasy()}"
        )

        for habarlandyru in self.habarlandyrushylar:
            habarlandyru.zhiberu(habar)

        print("Тапсырыс сәтті ресімделді!")


# Мысал
if __name__ == "__main__":
    indirim = IndirimEsepteu()
    indirim.ereje_qosu(PaizIndirim(7))
    indirim.ereje_qosu(TuraqtyIndirim(2000))

    habarlar = [
        EmailHabarlandyru("aset@example.com"),
        SmsHabarlandyru("+77001234567")
    ]

    qyzmet = TapsyrysQyzmeti(indirim, habarlar)

    tapsyrys = Tapsyrys("aset@example.com", "+77001234567")

    tapsyrys.onim_qosu(Onim("Xiaomi смартфоны", 120000), 1)
    tapsyrys.onim_qosu(Onim("Қап", 2500), 2)

    tapsyrys.tolem_tasin_tandau(KartamenTolem())
    tapsyrys.zhetkizu_tasin_tandau(KurerZhetkizu())

    print(f"Жеңілдіксіз сома: {tapsyrys.jalpy_soma:,.0f} теңге")
    qyzmet.tapsyrys_ornyndau(tapsyrys)