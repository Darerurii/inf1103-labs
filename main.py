from digital_product import DigitalProduct
from file_handling import FileHandling
from inventory import Inventory
from physical_product import PhysicalProduct
from product_logic import product_from_dict


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
 
def get_float(prompt, label):
    input_value = input(prompt).strip()
    try:
        value = float(input_value)
    except ValueError:
        print(f"Invalid {label}. Please enter a number.")
        return None
    if value < 0:
        # Capitalize instead of UPPER to ensure,
        # only first letter is capitalized in the error message
        print(f"{label.capitalize()} cannot be negative.")
        return None
    return value

def get_price():
    return get_float("Enter Price: ", "price")

def get_product_type():
    print("Select Product Type:")
    print("  1. Physical Product")
    print("  2. Digital Product")
    choice = input("Enter type: ").strip()
    if choice == "1":
        return PhysicalProduct.TYPE
    if choice == "2":
        return DigitalProduct.TYPE
    print("Invalid product type. Please enter 1 or 2.")
    return None

def create_product(product_type, product_id, name, price, quantity):
    if product_type == PhysicalProduct.TYPE:
        weight = get_float("Enter Weight (kg): ", "weight")
        if weight is None:
            return None
        return PhysicalProduct(product_id, name, price, quantity, weight)

    if product_type == DigitalProduct.TYPE:
        size = get_float("Enter Download Size (MB): ", "download size")
        if size is None:
            return None
        return DigitalProduct(product_id, name, price, quantity, size)

    return None

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
    
    # Check for product type, price, and quantity only if the product does not already exist
    product_type = get_product_type()
    if product_type is None:
        print("Invalid input. Product not added.")
        return
    
    price = get_price()
    quantity = get_quantity("Enter Quantity: ") if price is not None else None
    if price is None or quantity is None:
        print("Invalid input. Product not added.")
        return

    product = create_product(product_type, inventory.generate_id(), name, price, quantity)
    if product is None:
        print("Invalid input. Product not added.")
        return
    
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
        product.display_information()
    else:
        print("Product not found.")
 
 
def save_inventory_menu(inventory, file_handler):
    data = [product.to_dict() for product in inventory.get_products()]
    if file_handler.save_file(data):
        print(f"Inventory saved to {file_handler.get_filename()} successfully.")


def load_inventory(inventory, file_handler):
    for product_data in file_handler.load_file():
        try:
            inventory.add_product(product_from_dict(product_data))
        except (KeyError, ValueError) as error:
            #Ignore any errors when loading products from the file, 
            # as they may be due to missing or invalid data
            pass
 
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
    load_inventory(inventory, file_handler)

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