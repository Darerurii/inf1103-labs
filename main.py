from file_handling import FileHandling
from inventory import Inventory
from product import Product


def get_product_name():
    name = input("Enter Product Name: ").strip()
    if not name:
        print("Product name cannot be empty. Please enter a valid product name.")
        return None
    if any(char.isdigit() for char in name):
        print("This is an invalid format, please only input letters!!")
        return None
    return name
 
 
def get_quantity(prompt):
    value = input(prompt).strip()
    if not value.isdigit():
        print("This is an invalid format, please only input positive numbers!!")
        return None
    return int(value)
 
 
def get_price():
    value = input("Enter Price: ").strip()
    try:
        price = float(value)
    except ValueError:
        print("Invalid price. Please enter a number.")
        return None
    if price < 0:
        print("Price cannot be negative.")
        return None
    return price

def add_product_menu(inventory):
    name = get_product_name()
    if name is None:
        print("Invalid input. Product not added.")
        return
 
    existing = inventory.search_by_name(name)
    if existing:
        quantity = get_quantity("Enter Quantity: ")
        if quantity is None:
            print("Invalid input. Product not added.")
            return
        inventory.update_stock(existing.get_id(), quantity)
        print(f"{existing.get_name()} already exists. Stock updated to {existing.get_stock()}.")
        return

    price = get_price()
    quantity = get_quantity("Enter Quantity: ") if price is not None else None
    if price is None or quantity is None:
        print("Invalid input. Product not added.")
        return
    product = Product(inventory.generate_id(), name, price, quantity)
    inventory.add_product(product)
    print(f"New Product Added: {product.get_name()} (ID: {product.get_id()})")

def update_stock_menu(inventory):
    product_id = input("Enter Product ID to update stock: ")
    quantity = get_quantity("Enter Quantity to add: ")
    if quantity is None:
        print("Invalid input. Stock not updated.")
        return
    product = inventory.update_stock(product_id, quantity)
    if product:
        print(f"Stock updated for Product ID: {product.get_id()}. New Stock: {product.get_stock()}")
    else:
        print("Product not found.")
 
 
def search_product_menu(inventory):
    product_id = input("Enter Product ID to search: ")
    product = inventory.search_product(product_id)
    if product:
        print(f"Product Found: {product}")
    else:
        print("Product not found.")
 
 
def save_inventory_menu(inventory, file_handler):
    data = [product.to_dict() for product in inventory.get_products()]
    if file_handler.save_file(data):
        print(f"Inventory saved to {file_handler.get_filename()} successfully.")
 
 
def show_menu():
    print("-------------Menu-------------")
    print("1. Display Inventory")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Quit")
    print("------------------------------")
 
def main():
    file_handler = FileHandling("inventory.json")
    inventory = Inventory()
    saved_products = file_handler.load_file()

    for product_data in saved_products:
        product = Product.from_dict(product_data)
        inventory.add_product(product)
 
    while True:
        show_menu()
        choice = input("Enter option: ").strip()
        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":
            save_inventory_menu(inventory, file_handler)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")
 
 
if __name__ == "__main__":
    main()