amount_due = 50
cents = 0

while True:
    coin = int(input("Insert Coin: "))

    if coin not in [5, 10, 25]:
        print("Sorry, that coin is not accepted.")
        continue

    cents -= coin # Correct the subtraction
    amount_due -= coin

    if cents >= amount_due:
        print("Enjoy your Coke!")
        break

    print(f"Amount Due: {amount_due}")

if cents < amount_due:
    print(f"Change Owed: {amount_due - cents}")
