import json

rejected =0
state = 0
delivery = 0
totaltax=0
INVENTORY_FILE= "inventory.json"
FIELD_SEPARATOR = ","
HISTORY_SEPARATOR = "|"
MENU_OPTIONS = ("1", "2", "3", "4", "5", "6")

def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            inventory = json.load(file)
            print(inventory)
            return inventory
    except FileNotFoundError:
        return []    
    
def get_valid_input():
    product_name = input("Enter Product Name: ").strip()

    if product_name.lower() == "quit":
        return None,None
    
    elif any(char.isdigit() for char in product_name):
        print("This is an invalid format, please only input letters!!")
        # Process rejected entries count
        global rejected #makes rejected count a global variable so it can be accessed outside the function
        rejected += 1
        return None,None
    
    elif not product_name:
        print("Product name cannot be empty. Please enter a valid product name.")
        return None,None
    
    stock_number = input("Enter Quantity: ")
        
    # Check for end condition
    if stock_number.lower() == "quit":
        state = -1
        return None,None 



    # Check if the input is valid
    elif not stock_number.isdigit() or int(stock_number) < 0:
        print("This is an invalid format, please only input positive numbers!!")
        return None,None
            
    else:
        return str(product_name), int(stock_number)

def search_product(inventory, product_id):
    for item in inventory:
        if item["id"] == product_id:
            return item
    return None
def update_stock(inventory, product_name, stock_number):
    input_item = search_product(inventory, product_name)
    if input_item:
        input_item["stock"] += stock_number
        input_item["history"].append(stock_number)
        return True
    else:
        return False
    
def add_product(inventory, product_name, stock_number):
    input_item = search_product(inventory, product_name)
    if input_item != None:
        update_stock(inventory, product_name, stock_number)
    else:
        new_item = {
            "id": f"P{len(inventory)+1:03d}",
            "name": product_name,
            "stock": stock_number,
            "history": [stock_number]
        }
        inventory.append(new_item)
        print(inventory)
        print(f"New Product Added: {new_item['name']}")

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for item in inventory:
        print(f"ID: {item['id']}, Name: {item['name']}, Stock: {item['stock']}, History: {item['history']}")

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent = 4)
        print(f"Inventory saved to {INVENTORY_FILE} successfully.")

def main_menu(inventory):
    while True:
        print("-------------Menu-------------")
        print("1. Display Inventory")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Quit")
        print("------------------------------")
        input_choice = input("Enter option: ")
        if input_choice in MENU_OPTIONS:
            if input_choice == "1":
                    display_inventory(inventory)
            elif input_choice == "2":
                product_name, stock_number = get_valid_input()
                if product_name and stock_number is not None:
                    add_product(inventory, product_name, stock_number)
                else:
                    print("Invalid input. Product not added.")
            elif input_choice == "3":
                id = input("Enter Product ID to update stock: ")
                stock_number = input("Enter Quantity to add: ")
                if stock_number.isdigit() and int(stock_number) >= 0:
                    search_result = search_product(inventory, id)
                    if search_result:
                        update_status=update_stock(inventory, id, int(stock_number))
                        if update_status==True:
                            print(f"Stock updated for Product ID: {id}. New Stock: {search_result['stock']}")
                        else:
                            print("Failed to update stock.")
                    else:
                        print("Product not found.")
                else:
                    print("Invalid input. Stock not updated.")
            elif input_choice == "4":
                id = input("Enter Product ID to search: ")
                search_result = search_product(inventory, id)
                if search_result:
                    print(f"Product Found: ID: {search_result['id']}, Name: {search_result['name']}, Stock: {search_result['stock']}, History: {search_result['history']}")
                else:
                    print("Product not found.")
            elif input_choice == "5":
                save_inventory(inventory)
            elif input_choice == "6":
                print("Exiting the program.")
                return True  # Return True to indicate quitting
        else:
            print("Invalid option. Please try again.")
            continue
    
quit_program = False
while quit_program == False:
    quit_program = main_menu(load_inventory())