from abc import ABC, abstractmethod
from typing import Dict, List, Set


class IObserver(ABC):
    @abstractmethod
    def update(self, symbol: str, price: float):
        pass


class ISubject(ABC):
    @abstractmethod
    def attach(self, observer: IObserver, symbol: str):
        pass

    @abstractmethod
    def detach(self, observer: IObserver, symbol: str):
        pass

    @abstractmethod
    def notify(self, symbol: str):
        pass


class StockExchange(ISubject):
    def __init__(self):
        self.prices: Dict[str, float] = {}
        self.observers: Dict[str, Set[IObserver]] = {}

    def attach(self, observer: IObserver, symbol: str):
        if symbol not in self.observers:
            self.observers[symbol] = set()
        self.observers[symbol].add(observer)

    def detach(self, observer: IObserver, symbol: str):
        if symbol in self.observers:
            self.observers[symbol].discard(observer)

    def notify(self, symbol: str):
        if symbol in self.observers:
            price = self.prices.get(symbol, 0)
            for observer in list(self.observers[symbol]):
                observer.update(symbol, price)

    def update_price(self, symbol: str, new_price: float):
        self.prices[symbol] = new_price
        self.notify(symbol)


class ConsoleTrader(IObserver):
    def update(self, symbol: str, price: float):
        print(f"[Трейдер] {symbol} → {price:,.2f} ₸")


class AutoBot(IObserver):
    def __init__(self, buy_below: float = None, sell_above: float = None):
        self.buy_below = buy_below
        self.sell_above = sell_above

    def update(self, symbol: str, price: float):
        if self.buy_below is not None and price <= self.buy_below:
            print(f"[Бот] ПОКУПКА {symbol} по {price:,.2f} ₸")
        if self.sell_above is not None and price >= self.sell_above:
            print(f"[Бот] ПРОДАЖА {symbol} по {price:,.2f} ₸")


if __name__ == "__main__":
    exchange = StockExchange()

    trader1 = ConsoleTrader()
    bot_kaspi = AutoBot(buy_below=45000, sell_above=52000)
    bot_halyk = AutoBot(buy_below=32000)

    exchange.attach(trader1, "KSPI")
    exchange.attach(trader1, "HSBK")
    exchange.attach(bot_kaspi, "KSPI")
    exchange.attach(bot_halyk, "HSBK")

    print("Изменение цен:\n")

    exchange.update_price("KSPI", 48000)
    exchange.update_price("HSBK", 31000)
    exchange.update_price("KSPI", 53500)
    exchange.update_price("HSBK", 34000)