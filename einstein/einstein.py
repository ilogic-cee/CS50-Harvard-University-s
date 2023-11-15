def main():

    # Prompt the user for mass in kilograms
    mass = int(input("Enter mass in kilograms: "))

    # Convert mass to energy using the formula E = mc^2
    c = 299792458  # Speed of light in meters per second
    energy = mass * c ** 2

    # Print the energy in Joules
    print(f"Equivalent energy in Joules: {energy}")

if __name__ == "__main__":
    main()
