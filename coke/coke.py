# Initialize variables
amount_due = 0

# Prompt the user to insert a coin until the amount due is at least 50 cents
while amount_due < 50:
    # Get user input for the coin
    coin = int(input("Insert Coin: "))

    # Check if the coin is a valid denomination
    if coin == 25:
        # Update the amount due for 25 cents
        amount_due += coin
    elif coin == 10:
        # Update the amount due for 10 cents
        amount_due += coin
    elif coin == 5:
        # Update the amount due for 5 cents
        amount_due += coin
    else:
        # Print an error message for invalid coins
        print("Invalid Coin. Accepted denominations: 25, 10, 5 cents.")

    # Print the updated amount
    print(f"Amount Due: {amount_due}")

# Calculate and print the change owed
change_owed = amount_due - 50
print(f"Change Owed: {change_owed}")
