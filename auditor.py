inventory = 0
rejected = 0

while True:
    stock_input = input("Enter the Stock Quantity here: ").strip()
    
    # Check for end condition
    if stock_input.lower() == "quit":
        break

    # Check if the input is valid
    elif not stock_input.isdigit() or int(stock_input) < 0:
        print("This is an invalid format, please only input positive numbers!!")
        #Process rejected entries count
        rejected += 1
        
    # Process running inventory
    else:
        inventory += int(stock_input)
        
        # Check inventory capacity limit
        if inventory > 500:
            #Print Overcapacity Alert
            print("You have exceeded the maximum capacity for stock!!")
            break

# Print End Statistics
print(f"Total Units Processed: {inventory}")
print(f"Number of Rejected Entries: {rejected}")