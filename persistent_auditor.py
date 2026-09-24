rejected =0
state = 0
delivery = 0
totaltax=0
def load_inventory():
    try:
        with open("orders.txt", "r") as file:
            inventory = file.read().splitlines()
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


def save_inventory(inventory):
    with open("orders.txt", "w") as file:
        for item in inventory:
            file.write(f"{item}\n")
    print("Orders saved to orders.txt successfully.")

inventory = load_inventory()
delivery = sum(int(x.strip()) for x in inventory[2::3])  # Sum the quantities from the inventory list
totaltax=calculate_tax(delivery)
while state != -1:   
    product_name, stock_number, state = get_valid_input()
    
    # Check for end condition
    if state == -1 or product_name is None or stock_number is None:
        continue  # Skip processing if the user chose to quit or input was invalid

    # Process running delivery total
    else:
        if product_name in inventory:
            inventory[inventory.index(product_name)+1] += stock_number
        else:
            inventory.append(f"100{len(inventory)//3}")  # Assign a new stock number based on the current inventory size
            inventory.append(product_name)
            inventory.append(stock_number)
        tax=calculate_tax(stock_number)
        totaltax+=tax
        delivery = process_delivery(delivery, stock_number)
        if delivery > 500:
            print("Delivery exceeds 500 units!! Stopping further processing.")
            break  # Stop processing if delivery exceeds 500 units

# Print End Statistics
save_inventory(inventory)
print(inventory)
generate_report(delivery, rejected, totaltax)