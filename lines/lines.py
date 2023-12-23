import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Incorrect number of command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

    print(count_lines(sys.argv[1]))


def count_lines(file):
    try:
        with open(file, "r") as f:
            counter = sum(1 for line in f if not line.lstrip().startswith("#") and not line.isspace())
        return counter
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
