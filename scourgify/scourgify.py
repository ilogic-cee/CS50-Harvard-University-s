import csv
import sys

def main():
    """Main function to check command-line arguments and call the clean function."""
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])

def clean(input_file, output_file):
    """Reads the input CSV file, cleans the data, and writes the result to the output CSV file."""
    try:
        with open(input_file) as input_file:
            reader = csv.DictReader(input_file)
            with open(output_file, "w") as output_file:
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames=header)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

if __name__ == "__main__":
    main()
