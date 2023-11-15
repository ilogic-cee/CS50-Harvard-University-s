def main():
    # Prompt the user for mass
    mass = int(input("Enter mass in kilograms: "))

    # Convert mass to energy
    energy = mass * 299792458**2

    # Print the energy
    print(f"Energy in Joules: {energy}")

if __name__ == "__main__":
    main()
