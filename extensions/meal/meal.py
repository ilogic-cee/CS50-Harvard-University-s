# meal.py

def main():
    # Prompt the user for a time
    user_time = input("Enter a time (24-hour format): ")

    # Convert the user input to the corresponding number of hours
    time_in_hours = convert(user_time)

    # Determine the meal time based on the converted time
    determine_meal_time(time_in_hours)

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time.split(':'))

    # Calculate the corresponding number of hours as a float
    return hours + minutes / 60.0

def determine_meal_time(time_in_hours):
    # Define the meal time ranges
    breakfast_range = (7.0, 8.0)
    lunch_range = (12.0, 13.0)
    dinner_range = (18.0, 19.0)

    # Check if it's breakfast, lunch, or dinner time
    if breakfast_range[0] <= time_in_hours <= breakfast_range[1]:
        print("breakfast time")
    elif lunch_range[0] <= time_in_hours <= lunch_range[1]:
        print("lunch time")
    elif dinner_range[0] <= time_in_hours <= dinner_range[1]:
        print("dinner time")

if __name__ == "__main__":
    main()
