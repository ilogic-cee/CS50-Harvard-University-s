def main():
    # Initialize an empty dictionary to store items and their counts
    items = {}

    # Continue prompting for items until the user hits Ctrl+D
    while True:
        try:
            # Input the item
            item = input("Enter an item: ").lower()

            # Add the item to the dictionary, or increment its count if it already exists
            if item not in items:
                items[item] = 1
            else:
                items[item] += 1
        except EOFError:
            # Break out of the loop when Ctrl+D is pressed
            break

    # Sort the items dictionary by key (item name)
    sorted_items = sorted(items.items())

    # Print the grocery list, prefixing each line with the count and item name in uppercase
    for count, item in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
