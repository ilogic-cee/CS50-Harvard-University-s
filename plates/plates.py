def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    digits = 0

    valid = False
    while not valid:
        # minimum 2 and max 6 charcters(numbers and letters)
        if 2 <= len(s) <= 6 and s.isalnum():
            # if only 2 charcater then should only be letters
            if len(s) == 2 and not s.isalpha():
                valid = False
                break
            else:
                for i in s:
                    #if plate have digits value of digits variable gets updated accordingly
                    if i.isdigit():
                        digits += 1

                # checking condition one by one from character ranging 2 to 6
                if digits == 0 and len(s) >= 2:
                    valid = True
                    break

                if digits == 1 and s[-1].isdigit() and s[-1] != '0':
                    print(digits)
                    valid = True
                    break

                if digits == 2 and s[-2:].isdigit() and s[-2] != '0':
                    valid = True
                    break

                if digits == 3 and s[-3:].isdigit() and s[-3] != '0':
                    valid = True
                    break

                if digits == 4 and s[-4:] and s[-4] != '0':
                    valid = True
                    break

                else:
                    valid = False
                    break

        else:
            valid = False
            break

    return valid


main()
