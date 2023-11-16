# grocery.py

def main():
    grocery_list = {}

    try:
        while True:
            item = input("Enter an item (Ctrl-D to finish): ")
            item = item.lower()  # Convert input to lowercase

            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

    except EOFError:
        print_grocery_list(grocery_list)

def print_grocery_list(grocery_list):
    sorted_items = sorted(grocery_list.items())

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
