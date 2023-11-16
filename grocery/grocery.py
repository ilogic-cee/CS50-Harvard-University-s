from collections import Counter

def main():
    grocery_list = read_items()
    print_items(grocery_list)

def read_items():
    grocery_list = []
    try:
        while True:
            item = input("Enter an item: ").strip().upper()
            grocery_list.append(item)
    except EOFError:
        pass  # End of input

    return grocery_list

def print_items(grocery_list):
    item_counts = Counter(grocery_list)
    for item, count in item_counts.items():
        print(f"{count} {item}")

if __name__ == "__main__":
    main()
