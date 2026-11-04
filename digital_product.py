from product import Product

class DigitalProduct(Product):
    TYPE = "digital"

    def __init__(self, product_id, name, price, stock, download_size, history=None):
        super().__init__(product_id, name, price, stock, history)
        self.__download_size = float(download_size)

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self.__download_size:.2f} MB")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = self.TYPE
        data["download_size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data.get("price", 0.0),
            data["stock"],
            data.get("download_size", 0.0),
            data.get("history", [data["stock"]]),
        )
