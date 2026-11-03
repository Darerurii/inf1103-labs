from abc import ABC, abstractmethod
 
class Product(ABC):
    def __init__(self, product_id, name, price, stock, history=None):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__history = list(history) if history is not None else [self.__stock]

    @abstractmethod
    def placeholder(self):
        pass

    def get_id(self):
        return self.__product_id
 
    def get_name(self):
        return self.__name
 
    def get_price(self):
        return self.__price
 
    def get_stock(self):
        return self.__stock
 
    def get_history(self):
        return list(self.__history)

    def update_stock(self, quantity):
        if not self._validate_quantity(quantity):
            return False
        self.__stock += quantity
        self.__history.append(quantity)
        return True
 
    def _validate_quantity(self, quantity):
        return isinstance(quantity, int) and quantity >= 0
    

    def display_information(self):
        print(self)

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "history": list(self.__history),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data.get("price", 0.0),
            data["stock"],
            data.get("history", [data["stock"]]),
        )

    def __str__(self):
        return (f"ID: {self.__product_id}, Name: {self.__name}, "
                f"Price: ${self.__price:.2f}, Stock: {self.__stock}, "
                f"History: {self.__history}")