from abc import ABC, abstractmethod
from typing import Dict, List


class IObserver(ABC):
    @abstractmethod
    def update(self, currency: str, rate: float):
        pass


class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver):
        pass

    @abstractmethod
    def detach(self, observer: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass


class CurrencyExchange(ISubject):
    def __init__(self):
        self.rates: Dict[str, float] = {"USD": 480, "EUR": 520, "RUB": 5.1}
        self.observers: List[IObserver] = []

    def attach(self, observer: IObserver):
        self.observers.append(observer)

    def detach(self, observer: IObserver):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            for cur, rate in self.rates.items():
                observer.update(cur, rate)

    def update_rate(self, currency: str, new_rate: float):
        if currency in self.rates:
            self.rates[currency] = new_rate
            self.notify()


class BankMonitor(IObserver):
    def update(self, currency: str, rate: float):
        print(f"[Банк] Курс {currency}: {rate:,.2f} ₸")


class TraderBot(IObserver):
    def update(self, currency: str, rate: float):
        if currency == "USD" and rate > 495:
            print(f"[Трейдер] Продаём USD по {rate:,.2f} ₸")
        if currency == "EUR" and rate < 510:
            print(f"[Трейдер] Покупаем EUR по {rate:,.2f} ₸")


class NewsChannel(IObserver):
    def update(self, currency: str, rate: float):
        print(f"[Новости] Новый курс {currency} → {rate:,.2f} ₸")


if __name__ == "__main__":
    exchange = CurrencyExchange()

    bank = BankMonitor()
    trader = TraderBot()
    news = NewsChannel()

    exchange.attach(bank)
    exchange.attach(trader)
    exchange.attach(news)

    print("Обновление курсов:\n")

    exchange.update_rate("USD", 498.5)
    exchange.update_rate("EUR", 505.2)
    exchange.update_rate("RUB", 5.35)