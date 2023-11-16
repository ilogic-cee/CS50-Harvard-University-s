# taqueria.py

MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order_total = 0.00

    try:
        while True:
            item = input("Enter an item (Ctrl-D to finish): ")
            item = item.title()  # Convert input to title case

            if item in MENU:
                order_total += MENU[item]
                print(f"Total: ${order_total:.2f}")
            else:
                print("Invalid item. Please enter a valid item from the menu.")

    except EOFError:
        print("Order complete. Thank you!")

if __name__ == "__main__":
    main()
