# fuel.py

def main():
    while True:
        try:
            # Prompt the user for a fraction in the format X/Y
            fraction_input = input("Enter a fraction (X/Y): ")

            # Extract X and Y from the input
            x, y = map(int, fraction_input.split('/'))

            # Check for valid inputs
            if not (isinstance(x, int) and isinstance(y, int) and y > 0 and x <= y):
                raise ValueError("Invalid input. Please enter valid integers for X and Y, where X is less than or equal to Y.")

            # Calculate the percentage of fuel
            percentage = (x / y) * 100

            # Determine the output based on the percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")

            break  # Exit the loop if input and calculations are successful

        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
