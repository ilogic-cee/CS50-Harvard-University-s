# bank.py

def main():
    # Prompt the user for a greeting
    user_greeting = input("Enter a greeting: ")

    # Remove leading whitespace and convert the greeting to lowercase
    cleaned_greeting = user_greeting.lstrip().lower()

    # Check the conditions and output the corresponding amount
    if cleaned_greeting == "hello":
        print("$0")
    elif cleaned_greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
