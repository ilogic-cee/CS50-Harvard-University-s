def convert(text):
    # Replace :) with 🙂
    converted_text = text.replace(':)', '🙂')

    # Replace :( with 🙁
    converted_text = converted_text.replace(':(', '🙁')

    return converted_text

def main():
    # Prompt user for input
    user_input = input("Enter your text: ")

    # Convert the input
    converted_text = convert(user_input)

    # Print the converted text
    print(converted_text)

# Call the main function
if __name__ == "__main__":
    main()
