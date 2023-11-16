from collections import Counter

def main():
    groceries = read_items()
    print_grocery_list(groceries)

def read_items():
    groceries = []
    try:
        while True:
            item = input("Enter an item: ").strip().upper()
            groceries.append(item)
    except EOFError:
        return groceries

def print_grocery_list(groceries):
    counter = Counter(groceries)
    for item, count in counter.items():
        print(f"{count} {item}")

if __name__ == "__main__":
    main()
