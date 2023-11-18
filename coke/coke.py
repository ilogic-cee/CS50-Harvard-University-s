amount_due = 50
cents = 0

while cents < amount_due:
    # Check for valid coin before entering loop
    coin = int(input("Insert Coin: "))

    if coin not in [5, 10, 25]:
        print("Sorry, that coin is not accepted.")
        continue

    # Update cents and amount_due after accepting a valid coin
    cents -= coin
    amount_due -= coin
    print(f"Amount Due: {amount_due}")

if cents == amount_due:
    print("Enjoy your Coke!")
else:
    print(f"Change Owed: {amount_due - cents}")
