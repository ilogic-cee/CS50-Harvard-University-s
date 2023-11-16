# Initialize variables
amount_due = 0

# Prompt the user to insert a coin until the amount due is at least 50 cents
while amount_due < 50:
    # Get user input for the coin
    coin = int(input("Insert Coin: "))

    # Check if the coin is a valid denomination
    if coin == 25:
        amount_due += 25
    elif coin == 10:
        amount_due += 10
    elif coin == 5:
        amount_due += 5
    else:
        # Print an error message for invalid coins
        print("Invalid Coin. Accepted denominations: 25, 10, 5 cents.")

    # Print the updated amount
    print(f"Amount Due: {amount_due}")

    # Check if the user paid exactly 50 cents
    if amount_due == 50:
        print("Thank you for your purchase!")
        break
    elif amount_due > 50:
        # Calculate and print the change owed
        change_owed = max(0, amount_due - 50)
        print(f"Change Owed: {change_owed}")
        break
