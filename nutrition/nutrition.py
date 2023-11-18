def main():
    # FDA's poster for fruits and their calories
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        # Add more fruits and their calorie information as needed
    }

    # Prompt the user to input a fruit
    fruit_input = input("Enter a fruit: ").lower()

    # Check if the input is a valid fruit
    if fruit_input in fruit_calories:
        # Output the number of calories in one portion of that fruit
        print(f"Calories: {fruit_calories[fruit_input]}")
    else:
        # Ignore input that isn't a fruit
        print("Invalid fruit")

if __name__ == "__main__":
    main()
