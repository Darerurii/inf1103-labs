delivery = 0
rejected = 0
totaltax=0
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory = file.readlines()
            return inventory
    except FileNotFoundError:
        return []    
    
def get_valid_input():
    inventory = input("Enter the Stock Quantity here: ").strip()
        
    # Check for end condition
    if inventory.lower() == "quit":
        return -1  # Return -1 to indicate quitting

    # Check if the input is valid
    elif not inventory.isdigit() or int(inventory) < 0:
        print("This is an invalid format, please only input positive numbers!!")
        # Process rejected entries count
        global rejected #makes rejected count a global variable so it can be accessed outside the function
        rejected += 1
        state=-1
        return 0 
            
    else:
        return int(inventory)

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

while inventory != -1:
    inventory = get_valid_input()
    tax=calculate_tax(inventory)
    totaltax+=tax
    
    # Check for end condition
    if inventory == -1:
        break

    # Process running delivery total
    else:
        delivery = process_delivery(delivery, inventory)
        if delivery > 500:
            print("Delivery exceeds 500 units!! Stopping further processing.")
            break  # Stop processing if delivery exceeds 500 units

# Print End Statistics
generate_report(delivery, rejected, totaltax)