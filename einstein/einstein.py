# einstein.py

# Constants
speed_of_light = 300000000  # meters per second

# Function to calculate energy from mass
def calculate_energy(mass):
    energy = mass * speed_of_light**2
    return energy

# Main program
if __name__ == "__main__":
    # Prompt user for mass as an integer
    mass = int(input("Enter mass (in kilograms): "))

    # Calculate energy using Einstein's formula
    energy = calculate_energy(mass)

    # Output the equivalent energy in Joules
    print(energy)
