from random import choice

def main()
    number = choice((list(range(1, get_level()+1))))
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < number:
                    print("Too small!")
                    elif guess > number:
                    print("Too Large!")
                elif guess == number:
              sys.exit("Just Right!")
                    break
            except ValueError: 
                pass

        def get_level():
            while True:
                try:
                    level = int(input("Level: "))
                    if level > 0:
                        return level
                except ValueError:
                    pass

                main()

