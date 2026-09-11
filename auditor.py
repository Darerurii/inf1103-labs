inventory =0 
rejected = 0
while True:
    stock_input = input("Enter stock quantity (or type 'quit' to finish): ")

    # Check for the end condition
    if stock_input.lower() == 'quit':
        break
     # Check if the input is valid
    elif not stock_input.isdigit() or int(stock_input) < 0:
        print("This is an invalid format, please only input positive numbers!!")
    # Process running inventory
    else:
        inventory += int(stock_input)
