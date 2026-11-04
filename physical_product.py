from can_be_shipped import CanBeShipped
from product import Product


class PhysicalProduct(Product, CanBeShipped):
    TYPE = "physical"
    RATE_PER_KG = 2.00

    def __init__(self, product_id, name, price, stock, weight, history=None):
        # Reuse parent product init
        super().__init__(product_id, name, price, stock, history)
        self.__weight = float(weight)
    
    def get_weight(self) -> float:
        return self.__weight

    # Overrides Product.display_information()
    def display_information(self):
        # Reuse parent display_information() 
        super().display_information()
        print(f"Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self) -> str:
        return "Product requires physical shipping."
    
    def calculate_shipping_cost(self) -> float:
        return self.RATE_PER_KG * self.__weight
    
    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data.get("price", 0.0),
            data["stock"],
            data.get("weight", 0.0),
            data.get("history", [data["stock"]]),
        )
