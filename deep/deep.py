# deep.py

def main():
    # Prompt the user for the answer to the Great Question
    user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

    # Check if the input is 42 or equivalent (case-insensitive)
    if user_input.strip().lower() == "42" or user_input.strip().lower() == "forty-two" or user_input.strip().lower() == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
