def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if the plate has at least two letters
    if len(s) < 2 or not s[:2].isalpha():
        return False

    # Check if the plate has no more than 6 characters
    if len(s) > 6:
        return False

    # Check if numbers come at the end and the first number is not '0'
    if s[-1].isdigit() and s[2].isdigit() and s[2] == '0':
        return False

    # Check if there are no periods, spaces, or punctuation marks
    if any(char in ". ,;:!?" for char in s):
        return False

    return True


if __name__ == "__main__":
    main()
