import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print("Please enter a valid level (1, 2, or 3).")
            continue

        if level not in [1, 2, 3]:
            print("Please enter a valid level (1, 2, or 3).")
            continue

        return level


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level")

    return random.randint(0, 10 ** level - 1)


def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)

        for _ in range(3):
            answer = input(f"{num1} + {num2} = ")

            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
                continue

            if answer == num1 + num2:
                print("Correct!")
                correct_answers += 1
                break
            else:
                print("EEE")

        if answer != num1 + num2:
            print(f"{num1} + {num2} = {num1 + num2}")

    print(f"Score: {correct_answers} / 10")


if __name__ == "__main__":
    main()
