import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        print("Please enter a positive integer.")
        continue

    if level < 1:
        print("Please enter a positive integer.")
        continue

    secret_number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Please enter a positive integer.")
            continue

        if guess < 1:
            print("Please enter a positive integer.")
            continue

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            exit()
