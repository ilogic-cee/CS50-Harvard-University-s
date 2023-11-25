import sys

# Initialize an empty list to store names
names = []

# Prompt the user for names until they enter control-d
while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:
        break

# Construct the farewell message
farewell_message = ""
for i, name in enumerate(names):
    if i == len(names) - 1:
        farewell_message += "and " + name
    elif i == len(names) - 2:
        farewell_message += name
    else:
        farewell_message += name + ", "

farewell_message = "Adieu, adieu, to " + farewell_message

# Print the farewell message
print(farewell_message)
