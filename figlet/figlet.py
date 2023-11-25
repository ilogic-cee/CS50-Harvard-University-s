import sys
import random
from pyfiglet import Figlet
import cs50

# Check if the user provided zero or two command-line arguments
if len(sys.argv) not in [1, 3]:
    print("Invalid usage")
    sys.exit(1)

# Check if the first argument is a valid font selection command
if len(sys.argv) == 3 and sys.argv[1] not in ["-f", "--font"]:
    print("Invalid usage")
    sys.exit(1)

# Get the font name
font_name = sys.argv[2] if len(sys.argv) == 3 else random.choice(Figlet.getFonts())

# Prompt the user for input text
text = cs50.get_string("Input: ")

# Create a Figlet object and set the font
figlet = Figlet(font=font_name)

# Render the input text and print it
rendered_text = figlet.renderText(text)
print(rendered_text)
