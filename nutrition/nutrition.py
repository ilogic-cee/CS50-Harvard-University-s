def main():
    # FDA's poster for fruits and their calories
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "sweet cherries": 100,
        "kiwifruit": 90,
        "pear": 100,
        # Add more fruits and their calorie information as needed
    }

    # Prompt the user to input a fruit
    fruit_input = input("Enter a fruit: ").lower()

    # Get the calorie value for the input fruit, defaulting to None if not found
    calorie_value = fruit_calories.get(fruit_input, None)

    # Check if the input is a valid fruit
    if calorie_value is not None:
        # Output the number of calories in one portion of that fruit
        print(f"Calories: {calorie_value}")
    else:
        # Ignore input that isn't a fruit

if __name__ == "__main__":
    main()
