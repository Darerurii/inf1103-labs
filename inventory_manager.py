import json

rejected =0
state = 0
delivery = 0
totaltax=0
INVENTORY_FILE= "inventory.json"
FIELD_SEPARATOR = ","
HISTORY_SEPARATOR = "|"

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
        state = -1
        return None,None, state
    
    elif any(char.isdigit() for char in product_name):
        print("This is an invalid format, please only input letters!!")
        # Process rejected entries count
        global rejected #makes rejected count a global variable so it can be accessed outside the function
        rejected += 1
        return None,None, 0
    
    elif not product_name:
        print("Product name cannot be empty. Please enter a valid product name.")
        return None,None, 0
    
    stock_number = input("Enter Quantity: ")
        
    # Check for end condition
    if stock_number.lower() == "quit":
        state = -1
        return None,None, state  # Return -1 to indicate quitting



    # Check if the input is valid
    elif not stock_number.isdigit() or int(stock_number) < 0:
        print("This is an invalid format, please only input positive numbers!!")
        # Process rejected entries count
        rejected += 1
        return None,None, 0
            
    else:
        return str(product_name), int(stock_number), 0

#Process the delivery amount and update the total
def process_delivery (current_total, new_value):
    current_total += new_value
    return current_total

#Calculate tax based on the delivery amount
def calculate_tax(delivery):
    if delivery > 0:
        tax_rate = 0.10  # Example tax rate of 10%
        return delivery * tax_rate
    else:
        return 0

# Generates a report of the total units processed, number of rejected entries, and estimated tax on delivery
def generate_report(delivery, rejected, totaltax):
    print(f"Total Deliveries Processed: {delivery}")
    print(f"Number of Rejected Entries: {rejected}")
    print(f"Estimated Tax on Delivery: {totaltax:.2f}")

def search_product(inventory, product_name):
    for item in inventory:
        if item["name"] == product_name:
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
    
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent = 4)
        print(f"Inventory saved to {INVENTORY_FILE} successfully.")

