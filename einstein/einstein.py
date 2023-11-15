def main():
    # Prompt the user for mass in kilograms
    mass = int(input("Enter mass in kilograms: "))

    # Compute the equivalent number of Joules
    joules = mass * (299792458 ** 2)

    # Print the equivalent number of Joules
    print(f"Equivalent energy in Joules: {joules}")

if __name__ == "__main__":
    main()
