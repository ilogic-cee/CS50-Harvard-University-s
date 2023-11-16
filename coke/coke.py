def main():
    # Initialize variables
    coke_price = 50
    cents_inserted = 0

    # Prompt the user for coins until the price is met or exceeded
    while cents_inserted < coke_price:
        # Prompt the user for a coin denomination
        coin_denomination = int(input("Insert Coin: "))

        # Check if the coin denomination is accepted
        if coin_denomination in [25, 10, 5]:
            cents_inserted += coin_denomination
            print(f"Amount Due: {cents_inserted}")
        else:
            print("Invalid coin denomination. Please try again.")

    # Calculate the change owed
    change_owed = coke_price - cents_inserted

    # Print the change owed
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
