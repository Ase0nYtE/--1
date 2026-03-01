from abc import ABC, abstractmethod


class IPaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class CardPayment(IPaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Оплата картой: {amount:,.2f} ₸ → успешно")
        return True


class PayPalPayment(IPaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Оплата PayPal: {amount:,.2f} ₸ → успешно")
        return True


class CryptoPayment(IPaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Оплата криптовалютой: {amount:,.2f} ₸ → успешно")
        return True


class PaymentContext:
    def __init__(self, strategy: IPaymentStrategy = None):
        self.strategy = strategy

    def set_strategy(self, strategy: IPaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount: float):
        if self.strategy is None:
            print("Способ оплаты не выбран!")
            return
        success = self.strategy.pay(amount)
        print("Платёж успешен" if success else "Платёж не удался")


if __name__ == "__main__":
    context = PaymentContext()

    context.set_strategy(CardPayment())
    context.execute_payment(12500)

    context.set_strategy(PayPalPayment())
    context.execute_payment(8900)

    context.set_strategy(CryptoPayment())
    context.execute_payment(45000)