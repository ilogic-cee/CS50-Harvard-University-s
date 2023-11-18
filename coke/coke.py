amount_due = 50
cents = 0

while cents < amount_due:
    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        cents += coin
        print(f"Amount Due: {cents}")
    else:
        print("Sorry, that coin is not accepted.")

print(f"Change Owed: {amount_due - cents}")
