class Inventory:
     
    def __init__(self):
            self.__products = []
    
    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id().upper() == product_id.strip().upper():
                return product
        return None

    def search_by_name(self, name):
        for product in self.__products:
            if product.get_name().lower() == name.strip().lower():
                return product
        return None

    def update_stock(self, product_id, quantity):
        # Allows the updating of stock for saved products
        product = self.search_product(product_id)
        # Needed to ensure only product class can update its own state.
        if product and product.update_stock(quantity):
            return product
        return None

    def display_all(self):
            print("\nCurrent Inventory:")
            if not self.__products:
                print("Inventory is empty.")
            for product in self.__products:
                product.display_information()

    def get_products(self):
        return list(self.__products)

    def generate_id(self):
        highest = 0
        for product in self.__products:
            digits = product.get_id()[1:]
            if digits.isdigit():
                highest = max(highest, int(digits))
        return f"P{highest + 1:03d}"