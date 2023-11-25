from random import choice

def main()
    number = choice((list(range(1, get_level()+1))))
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < number:
                    print("")
