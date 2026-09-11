inventory =0 
rejected = 0
while True:
    stock_input = input("Enter stock quantity (or type 'quit' to finish): ")

    # Check for the end condition
    if stock_input.lower() == 'quit':
        break
    
