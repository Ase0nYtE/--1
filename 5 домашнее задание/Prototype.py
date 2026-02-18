import copy
from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    name: str
    price: float
    quantity: int

@dataclass
class Discount:
    name: str
    amount: float

class Order:
    def __init__(self):
        self.products: List[Product] = []
        self.delivery_cost: float = 0.0
        self.discounts: List[Discount] = []
        self.payment_method: str = ""

    def add_product(self, product: Product):
        self.products.append(product)

    def add_discount(self, discount: Discount):
        self.discounts.append(discount)

    def clone(self) -> 'Order':
        return copy.deepcopy(self)

    def show_info(self):
        print("Order:")
        print(f"  Delivery: {self.delivery_cost}")
        print(f"  Payment: {self.payment_method}")
        if self.products:
            print("  Products:")
            for p in self.products:
                print(f"    - {p.name} (price {p.price}, quantity {p.quantity})")
        if self.discounts:
            print("  Discounts:")
            for d in self.discounts:
                print(f"    - {d.name} ({d.amount})")
        print("-" * 40)

if __name__ == "__main__":
    order_template = Order()
    order_template.delivery_cost = 500.0
    order_template.payment_method = "Card"
    order_template.add_product(Product("Book", 1000.0, 1))
    order_template.add_discount(Discount("New Year", 200.0))

    order1 = order_template.clone()
    order1.payment_method = "Cash"
    order1.add_product(Product("Toy", 500.0, 2))

    order_template.show_info()
    order1.show_info()