import sys
import random
from pyfiglet import Figlet
import cs50

#
#figlet = figlet()
commands = ["-f","-font"]
fonts = figlet.getFonts()

 if len(sys.argv) < 1:
    print("Usage: figlet [FONT] [TEXT]")
    sys.exit(1)

font = sys.argv[1] if len(sys.argv) > 2 else "standard"
text = sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read()

print(figlet.format_text(text, font=font))


    else:
        sys.exit("Invalid usage")

        string = cs50.get_string("Input: ")

            figlet.setFont(font= new_font)

            print(figlet.renderText(string))


