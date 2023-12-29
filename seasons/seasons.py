from datetime import date
import inflect
import sys

def main():
    try:
        dob_input = input("Enter your birthdate (YYYY-MM-DD): ")
        dob = date.fromisoformat(dob_input)

        # Ensure the birthdate is not in the future
        if dob > date.today():
            sys.exit("Birthdate cannot be in the future. Please enter a valid date.")

        age_in_days = (date.today() - dob).days
        print(f"You are {convert_days_to_minutes(age_in_days)} minutes old.")

    except ValueError:
        sys.exit("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def convert_days_to_minutes(days):
    p = inflect.engine()
    minutes = days * 24 * 60
    return p.number_to_words(minutes, andword='').capitalize() + " minutes"

if __name__ == "__main__":
    main()
