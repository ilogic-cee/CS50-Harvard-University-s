def main():
    amount_due = 0

    while amount_due < 50:
        try:
            coin = int(input("Insert Coin: "))
            if coin in [5, 10, 25]:
                amount_due += coin
                print(f"Amount Due: {amount_due}")
            else:
                print("Invalid coin. Accepted denominations: 5, 10, 25.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    change_owed = amount_due - 50
    print(f"Change Owed: {max(0, change_owed)}")

if __name__ == "__main__":
    main()
