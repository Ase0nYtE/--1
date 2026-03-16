from abc import ABC, abstractmethod

class IInternalDeliveryService(ABC):
    @abstractmethod
    def deliver_order(self, order_id: str) -> str:
        pass

    @abstractmethod
    def get_delivery_status(self, order_id: str) -> str:
        pass

class InternalDeliveryService(IInternalDeliveryService):
    def deliver_order(self, order_id: str) -> str:
        return f"Внутренняя доставка: заказ {order_id} отправлен"

    def get_delivery_status(self, order_id: str) -> str:
        return f"Внутренняя доставка: заказ {order_id} в пути"

class ExternalLogisticsServiceA:
    def ship_item(self, item_id: int) -> str:
        return f"Service A: товар {item_id} отгружен"

    def track_shipment(self, shipment_id: int) -> str:
        return f"Service A: трекинг {shipment_id} — доставляется"

class ExternalLogisticsServiceB:
    def send_package(self, package_info: str) -> str:
        return f"Service B: посылка {package_info} отправлена"

    def check_package_status(self, tracking_code: str) -> str:
        return f"Service B: статус {tracking_code} — в пункте выдачи"

class ExternalLogisticsServiceC:
    def dispatch(self, ref: str) -> str:
        return f"Service C: отправка {ref} выполнена"

    def query_status(self, ref: str) -> str:
        return f"Service C: {ref} — получено"

class LogisticsAdapterA(IInternalDeliveryService):
    def __init__(self, service: ExternalLogisticsServiceA):
        self.service = service

    def deliver_order(self, order_id: str) -> str:
        try:
            item_id = int(order_id.replace("ORD-", ""))
            return self.service.ship_item(item_id)
        except:
            return "Ошибка адаптера A: неверный формат номера заказа"

    def get_delivery_status(self, order_id: str) -> str:
        try:
            shipment_id = int(order_id.replace("ORD-", "")) + 1000
            return self.service.track_shipment(shipment_id)
        except:
            return "Ошибка адаптера A: неверный формат трекинга"

class LogisticsAdapterB(IInternalDeliveryService):
    def __init__(self, service: ExternalLogisticsServiceB):
        self.service = service

    def deliver_order(self, order_id: str) -> str:
        return self.service.send_package(f"Order-{order_id}")

    def get_delivery_status(self, order_id: str) -> str:
        return self.service.check_package_status(f"TRK-{order_id}")

class LogisticsAdapterC(IInternalDeliveryService):
    def __init__(self, service: ExternalLogisticsServiceC):
        self.service = service

    def deliver_order(self, order_id: str) -> str:
        return self.service.dispatch(order_id)

    def get_delivery_status(self, order_id: str) -> str:
        return self.service.query_status(order_id)

class DeliveryServiceFactory:
    @staticmethod
    def get_service(service_type: str) -> IInternalDeliveryService:
        if service_type == "internal":
            return InternalDeliveryService()
        elif service_type == "A":
            return LogisticsAdapterA(ExternalLogisticsServiceA())
        elif service_type == "B":
            return LogisticsAdapterB(ExternalLogisticsServiceB())
        elif service_type == "C":
            return LogisticsAdapterC(ExternalLogisticsServiceC())
        else:
            raise ValueError(f"Неизвестный тип службы: {service_type}")

if __name__ == "__main__":
    orders = ["ORD-123", "ORD-456", "ORD-789"]

    print("=== Внутренняя доставка ===")
    svc = DeliveryServiceFactory.get_service("internal")
    for o in orders:
        print(svc.deliver_order(o))
        print(svc.get_delivery_status(o))

    print("\n=== Служба A ===")
    svc = DeliveryServiceFactory.get_service("A")
    for o in orders:
        print(svc.deliver_order(o))
        print(svc.get_delivery_status(o))

    print("\n=== Служба B ===")
    svc = DeliveryServiceFactory.get_service("B")
    for o in orders:
        print(svc.deliver_order(o))
        print(svc.get_delivery_status(o))

    print("\n=== Служба C ===")
    svc = DeliveryServiceFactory.get_service("C")
    for o in orders:
        print(svc.deliver_order(o))
        print(svc.get_delivery_status(o))