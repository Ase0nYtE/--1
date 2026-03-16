from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

class PayPalPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"PayPal: успешно обработано {amount} ₸"

class StripePaymentService:
    def make_transaction(self, total_amount: float) -> str:
        return f"Stripe: транзакция на {total_amount} ₸ выполнена"

class AnotherPaymentGateway:
    def charge(self, value: float, currency: str = "KZT") -> str:
        return f"GatewayX: списано {value} {currency}"

class StripePaymentAdapter(IPaymentProcessor):
    def __init__(self, stripe_service: StripePaymentService):
        self.stripe = stripe_service

    def process_payment(self, amount: float) -> str:
        return self.stripe.make_transaction(amount)

class GatewayXAdapter(IPaymentProcessor):
    def __init__(self, gateway: AnotherPaymentGateway):
        self.gateway = gateway

    def process_payment(self, amount: float) -> str:
        return self.gateway.charge(amount)

if __name__ == "__main__":
    print("Оплата через PayPal:")
    paypal = PayPalPaymentProcessor()
    print(paypal.process_payment(12500.0))

    print("\nОплата через Stripe (адаптер):")
    stripe_adapter = StripePaymentAdapter(StripePaymentService())
    print(stripe_adapter.process_payment(8900.0))

    print("\nОплата через GatewayX (адаптер):")
    gateway_adapter = GatewayXAdapter(AnotherPaymentGateway())
    print(gateway_adapter.process_payment(45000.0))

    print("\nКомбинированный заказ:")
    payments = [
        PayPalPaymentProcessor(),
        StripePaymentAdapter(StripePaymentService()),
        GatewayXAdapter(AnotherPaymentGateway())
    ]

    total = 0.0
    for i, p in enumerate(payments, 1):
        amount = 5000.0 * i
        total += amount
        print(f"Часть {i}: {amount} ₸ → {p.process_payment(amount)}")
    print(f"\nИтого: {total} ₸")