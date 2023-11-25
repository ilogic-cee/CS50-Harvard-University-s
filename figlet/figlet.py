import sys
import random
from pyfiglet import Figlet
import cs50

#
#figlet = figlet()
commands = ["-f","-font"]
fonts = figlet.getFonts()

    if len(sys.argv) < 1:
        new_font = random.choice(fonts)


    if len(sys.argv) == 3 and sys.argv[2] in fonts and sys.argv[1] in commands:
        new_font = sys.argv[2]


    else:
        sys.exit("Invalid usage")

        string = cs50.get_string("Input: ")

            figlet.setFont(font= new_font)
            
            print(figlet.renderText(string))


