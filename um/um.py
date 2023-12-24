import re


def main():
    result = count(input("Text: "))
    if result is not None:
        print(result)
    else:
        print("No occurrences of 'um' found.")


def count(s):
    # Match if "um" is in the beginning (^) or end ($) of a string input
    # Match if the character before and after "um" is not alphanumeric (punctuation / space is ok)
    regex = "(^|\W)um($|\W)"
    match = re.findall(regex, s, re.IGNORECASE)
    if match:
        return len(match)
    else:
        return None


if __name__ == "__main__":
    main()
