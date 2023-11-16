# Initialize variables
amount_due = 0

# Prompt the user to insert a coin until the amount due is at least 50 cents
while amount_due < 50:
    # Get user input for the coin
    coin = int(input("Insert Coin: "))

    # Check if the coin is a valid denomination
    if coin == 25 or coin == 10 or coin == 5:
        # Update the amount due based on the denomination
        amount_due += coin

        # Print the updated amount
        print(f"Amount Due: {amount_due}")
    else:
        # Print an error message for invalid coins
        print("Invalid Coin. Accepted denominations: 25, 10, 5 cents.")

# Check if the user paid exactly 50 cents
if amount_due == 50:
    print("Thank you for your purchase!")
else:
    # Calculate and print the change owed
    change_owed = 50 - amount_due
    print(f"Change Owed: {max(0, change_owed)}")
            
